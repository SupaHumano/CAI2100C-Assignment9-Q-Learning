"""I verify my Assignment 9 results independently from the notebook and the website."""
from pathlib import Path
from collections import deque
from tempfile import TemporaryDirectory
import argparse
import json
import math
import re

import nbformat
from nbclient import NotebookClient
from PIL import Image
from pptx import Presentation

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / 'academic/CAI2100C_Assignment_9_Q_Learning_Juan_Luna_Santibanez.ipynb'
ROWS = ('...#####', '.#..G..#', '##.##...', '...#....',
        '.....##.', '...#.#..', '.#.#.#.#', '.....#.#')
STARTS = {'A': (1, 0), 'B': (7, 6), 'C': (4, 3)}
GOAL = (1, 4)
FIGURES = ('official_assignment_map', 'route_A', 'route_B', 'route_C',
           'three_routes', 'episode_comparison', 'learning_curve', 'q_value_heatmap')

def shortest(start):
    q = deque([(start, 0)])
    seen = {start}
    while q:
        (r, c), steps = q.popleft()
        if (r, c) == GOAL:
            return steps
        for dr, dc in ((0, 1), (-1, 0), (0, -1), (1, 0)):
            v = (r+dr, c+dc)
            if 0 <= v[0] < 8 and 0 <= v[1] < 8 and ROWS[v[0]][v[1]] != '#' and v not in seen:
                seen.add(v)
                q.append((v, steps+1))
    raise AssertionError('I cannot find a safe route from ' + str(start))

def validate_data(base):
    results = json.loads((base/'data/results.json').read_text(encoding='utf-8'))
    site = (base/'data/results.js').read_text(encoding='utf-8').strip()
    prefix = 'window.ASSIGNMENT9_RESULTS = '
    assert site.startswith(prefix) and site.endswith(';'), 'Missing browser data'
    assert json.loads(site[len(prefix):-1]) == results, 'JSON and JS disagree'
    assert tuple(results['map_rows']) == ROWS
    assert len(ROWS) == 8 and all(len(row) == 8 for row in ROWS)
    assert sum(row.count('#') for row in ROWS) == 22
    assert results['goal'] == list(GOAL)
    assert {k: tuple(v) for k,v in results['starts'].items()} == STARTS
    assert results['parameters']['episodes'] == 10000
    assert results['parameters']['seed'] == 2026
    assert set(results['routes']) == set(STARTS)
    for k, start in STARTS.items():
        route = results['routes'][k]
        path = [tuple(x) for x in route['path']]
        assert path[0] == start and path[-1] == GOAL, k
        assert len(path) == len(set(path)), 'Learned route contains a cycle'
        assert all(ROWS[r][c] != '#' for r,c in path), 'Learned route enters Cliff'
        assert all(abs(a[0]-b[0])+abs(a[1]-b[1]) == 1 for a,b in zip(path,path[1:]))
        assert route['status'] == 'goal' and route['valid'] and route['optimal']
        assert len(path)-1 == shortest(start) == route['steps'] == route['bfs_shortest_steps']
    assert [results['routes'][x]['steps'] for x in 'ABC'] == [6, 10, 6]
    budgets = results['episode_experiments']
    assert [x['episodes'] for x in budgets] == [50, 500, 2000, 10000]
    assert [x['optimal_starts'] for x in budgets] == [1,3,3,3]
    for x in budgets:
        assert math.isfinite(x['training_avg_reward_last_250'])
        assert 0 <= x['training_goal_rate_last_250'] <= 1
    assert [round(x['alpha'],2) for x in results['learning_rate_experiments']] == [0.1,0.3,0.7]
    return results

def verify_publication():
    results=validate_data(ROOT)
    for name in FIGURES:
        path=ROOT/'assets'/f'{name}.png'
        assert path.exists(), 'Missing figure ' + str(path)
        with Image.open(path) as img:
            assert img.width >= 700 and img.height >= 300
            img.verify()
    nb=nbformat.read(NOTEBOOK,as_version=4)
    codes=[cell for cell in nb.cells if cell.cell_type=='code']
    assert len(nb.cells)==22 and len(codes)==11
    assert all(isinstance(c.execution_count,int) for c in codes)
    assert not any(o.output_type=='error' for c in codes for o in c.get('outputs',[]))
    inline=sum(bool(o.get('data',{}).get('image/png')) for c in codes for o in c.get('outputs',[]))
    assert inline >= 8
    full='\n'.join(c.source for c in nb.cells)
    assert 'Juan Luna Santibanez' in full and 'Beth Muturi' in full
    assert '## 9. My answers to the professor' in full
    assert 'import gym' not in full and 'drive.mount(' not in full
    assert '\u2014' not in full
    page=(ROOT/'index.html').read_text(encoding='utf-8')
    assert 'data/results.js' in page and 'Assignment 9' in page
    for asset in re.findall(r'''(?:src|href)=['"]([^'"#]+)''', page):
        if asset.startswith(('http:', 'https:', 'mailto:','data:')):
            continue
        assert (ROOT/asset).exists(), 'Broken HTML link: '+asset
    qa=(ROOT/'docs/PRESENTATION_QA.md').read_text(encoding='utf-8')
    assert qa.count('### ') == 33
    assert (ROOT/'docs/ASSIGNMENT_REQUIREMENTS.md').is_file()
    assert (ROOT/'docs/METHODOLOGY.md').is_file()
    assert (ROOT/'docs/COLAB_GUIDE.md').is_file()
    deck=Presentation(str(ROOT/'presentation/Assignment_9_Presentation_Juan_Luna_Santibanez.pptx'))
    assert len(deck.slides)==7
    texts='\n'.join(sh.text for slide in deck.slides for sh in slide.shapes if sh.has_text_frame)
    assert 'Juan Luna Santibanez' in texts and 'Beth Muturi' in texts
    print('PASS: Official map, independently shortest safe routes, data, notebook, 33 Q&A and seven slides')
    return results

def verify_fresh_runtime(expected):
    with TemporaryDirectory(prefix='assignment9-colab-') as folder:
        target=Path(folder)
        notebook=nbformat.read(NOTEBOOK,as_version=4)
        executed=NotebookClient(notebook,kernel_name='python3',timeout=180,allow_errors=False,
                   resources={'metadata':{'path':str(target)}}).execute()
        assert sum(c.cell_type=='code' and isinstance(c.execution_count,int) for c in executed.cells)==11
        assert not any(o.output_type=='error' for c in executed.cells for o in c.get('outputs',[]))
        actual=validate_data(target)
        assert actual == expected, 'A clean standalone run altered the calculated data'
        for name in FIGURES:
            assert (target/'assets'/f'{name}.png').stat().st_size>10000
        print('PASS: I ran all 11 code cells from an empty directory with identical results')

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--fresh-runtime',action='store_true')
    args=parser.parse_args()
    expected=verify_publication()
    if args.fresh_runtime:
        verify_fresh_runtime(expected)
