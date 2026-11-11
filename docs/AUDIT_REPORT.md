# My Assignment 9: Preaudit and Postaudit

**Student:** Juan Luna Santibanez  
**Course:** CAI2100C-2267-6908, Machine Learning Foundations  
**Professor:** Beth Muturi  
**Audit date:** November 10, 2026

## Preaudit: I established the official requirements

I inspected `Assignment 9.zip`, the six-slide original `Assignment 9.pptx` and both reference notebooks. The original ZIP has 13 members. Its SHA-256 is `0d472169d644dd5a320f90f60418bc29cb01e286be9dfa09e0ebbf0dbf39a8b1`.

I confirmed that the official diagram on slide 5, rather than the smaller demonstration notebook, contains **8 rows, 8 columns, 22 Cliffs, 41 walkable squares and one Goal at (1, 4)**. My required starts are **(1, 0), (7, 6) and (4, 3)**. The professor asks for safe shortest paths, a traceable solution and an investigation of episode count and other parameters.

I also parsed the original slide 5 PowerPoint table programmatically and compared all **64 cells against the notebook map. All 64 positions matched exactly**.

I selected the **Q-Learning reference notebook** to guide the implementation. The bundled Gym notebook is extra learning material, not an additional required submission. I do not redistribute either instructor notebook in my portfolio.

## Postaudit 1: Scientific correctness

| Check | Result |
|---|---|
| Exact 8 × 8 course map | PASS |
| 22 Cliffs, 1 Goal, 41 walkable squares | PASS |
| Route A, (1, 0) | 6 steps, same minimum as BFS |
| Route B, (7, 6) | 10 steps, same minimum as BFS |
| Route C, (4, 3) | 6 steps, same minimum as BFS |
| No Cliff entry in final greedy paths | PASS, 3/3 |
| Every move within one adjacent square | PASS, 3/3 |
| Q-table learned from rewards, not BFS paths | PASS |
| Episode comparisons: 50, 500, 2,000, 10,000 | PASS |
| Learning-rate comparison at 2,000 episodes | PASS |

I use independent breadth-first search only to verify the shortest number of safe moves. The reference paths are not supplied to the reinforcement-learning algorithm.

## Postaudit 2: Execution and notebook portability

I executed my completed Jupyter notebook from beginning to end, then executed it a second time with Jupyter's notebook client in a **fresh, empty working directory**. I checked the generated JSON from the new run against the original saved results.

- **Notebook cells:** 22, with 11 code cells.
- **Executed code cells:** 11/11.
- **Recorded Python errors:** 0.
- **Inline figures:** 8.
- **External CSV or network download required:** none.
- **Local repository import or Google Drive mount required:** none.
- **Reproduced data and route outcomes:** exactly consistent across the two runs.

I use only NumPy, Matplotlib and Python standard-library modules inside the academic notebook. That makes the notebook suitable for upload to standard Google Colab and Jupyter runtimes. A successful local clean-runtime execution is not a claim that my notebook was opened in a separate Google Colab user account.

## Postaudit 3: Visual experience and academic clarity

I created the official-map figure, three individual route figures, one combined route map, an episode comparison, a learning-reward curve and a Q-value heatmap. My static website uses only those computed results.

I tested the interactive page in Chromium at **1440px, 768px and 390px**. I clicked all three starting-position controls at each width and verified **6, 10 and 6 movements**, zero Cliff collisions, correct route-length indicators and no JavaScript exceptions. I observed no horizontal overflow.

I also created a **7-slide optional presentation** for the tentative 5-to-10-minute classroom presentation described in slide 2, and a **33-question first-person defense guide**.

## What remains external

My public GitHub repository has been initialized, and my publication checks are tracked separately. The repository is publicly accessible at https://github.com/SupaHumano/CAI2100C-Assignment9-Q-Learning. GitHub Actions run 42928818197 completed successfully, executed the academic notebook, generated figures and the optional presentation, and passed the clean-runtime verification. I do not equate this scientific CI result with an independently verified public GitHub Pages deployment.

The exact Canvas deadline, group-submission settings and professor's final grading remain under the instructor's control. My report certifies the stated engineering checks, not a guaranteed grade.

**Verified local and GitHub Actions engineering status: PASS.** The only academic submission notebook is in `academic/`.