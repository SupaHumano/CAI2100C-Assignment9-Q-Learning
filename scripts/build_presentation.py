"""I generate my optional seven-slide presentation from the verified notebook figures."""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

root=Path(__file__).resolve().parents[1]
dest=root/'presentation/Assignment_9_Presentation_Juan_Luna_Santibanez.pptx'
dest.parent.mkdir(parents=True,exist_ok=True)
prs=Presentation()
prs.slide_width=Inches(13.333)
prs.slide_height=Inches(7.5)
bg=RGBColor(11,22,42)
white=RGBColor(243,248,255)
muted=RGBColor(174,190,211)
mint=RGBColor(85,213,174)
def tbox(slide,txt,x,y,w,h,size=21,bold=False,color=white):
    sh=slide.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    tf=sh.text_frame
    tf.word_wrap=True
    tf.text=txt
    for p in tf.paragraphs:
        p.font.size=Pt(size)
        p.font.bold=bold
        p.font.color.rgb=color
    return sh
def base(title,kicker):
    slide=prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb=bg
    tbox(slide,'CAI2100C | MACHINE LEARNING FOUNDATIONS',.55,.3,12,.32,11,True,mint)
    tbox(slide,title,.55,.84,12,.75,30,True)
    tbox(slide,kicker,.55,1.6,12,.6,14,False,muted)
    tbox(slide,'Juan Luna Santibanez | Professor Beth Muturi',.55,7.07,11,.28,10,False,muted)
    return slide
def fig(slide,path,x=.85,y=2.12,w=11.65):
    slide.shapes.add_picture(str(root/'assets'/path),Inches(x),Inches(y),width=Inches(w))
s=base('Assignment 9 | Learning to Navigate Safely','I use Q-Learning to find verified shortest routes on the official Cliff map.')
tbox(s,'I trained an agent rather than drawing a predefined route.',.85,3,11,1.1,29,True,mint)
tbox(s,'Juan Luna Santibanez | Miami Dade College',.85,4.7,10,.55,19)
s=base('My assignment and official environment','I reconstructed the exact 8 × 8 map with 22 Cliffs and Goal (1, 4).')
fig(s,'official_assignment_map.png',3.2,1.98,6.9)
s=base('How I trained the agent','I update state-action values from rewards and penalize entering a Cliff.')
tbox(s,'Rewards: Goal +100 | Cliff -100 | Normal move -1',.8,2.5,11,.6,24,True,mint)
tbox(s,'I use 10,000 episodes, α = 0.30, γ = 0.96 and a reproducible seed (2026).',.8,3.45,11,.95,23)
tbox(s,'BFS does not teach the agent. I use it only afterward to check optimality.',.8,4.75,11,.95,21)
s=base('Three required starting points','All three learned routes are safe and equal to independent BFS distances.')
fig(s,'three_routes.png',2.0,1.96,9.2)
s=base('Does training volume matter?','I compared four episode budgets under the same seed and parameters.')
fig(s,'episode_comparison.png',.75,2.16,11.7)
s=base('Inspecting how the model learns','I distinguish training rewards from the quality of the final greedy policy.')
fig(s,'learning_curve.png',.55,2.25,6.4)
fig(s,'q_value_heatmap.png',7.25,2.25,5.25)
s=base('My conclusion and academic verification','I confirmed each safe route using a separate shortest-path calculation.')
tbox(s,'(1, 0): 6 moves   |   (7, 6): 10 moves   |   (4, 3): 6 moves',.8,2.8,11,.9,25,True,mint)
tbox(s,'I verified every movement, avoided all 22 Cliffs and evaluated the episode count and learning rate.',.8,4.1,11,1,21)
tbox(s,'My result is a controlled classroom experiment, not a real autonomous-driving system.',.8,5.4,11,.85,18,False,muted)
prs.save(dest)
print('PASS: Created seven first-person presentation slides:',dest)
