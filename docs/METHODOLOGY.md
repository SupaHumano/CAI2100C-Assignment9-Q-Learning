# My Q-Learning methodology

**Juan Luna Santibanez | CAI2100C-2267-6908 | Professor Beth Muturi**

## My source and environment

I reconstructed the official 8 by 8 map on slide 5 of the Assignment 9 presentation, with 22 Cliff cells, 41 open cells and one Goal at (1, 4). I use zero-based (row, column) coordinates.

## My algorithm

I created a tabular Q-Learning agent with four actions, one per cardinal direction. I use +100 for reaching the Goal, -100 for entering a Cliff and -1 for a normal move, then terminate the episode at the Goal or Cliff. I do not eliminate Cliff actions during training; penalized outcomes provide information.

My main experiment uses 10,000 episodes, alpha 0.30, gamma 0.96, exploration decreasing from 0.60 to 0.03, and random seed 2026. I visit safe squares and repeatedly train from the three required starts.

## My independent mathematical cross-check

I use breadth-first search on the Cliff-free graph to compute a shortest path **after** training. BFS does not supply the training target. I verify that the greedy learned policy reaches the Goal, avoids Cliffs, moves one cell at a time and matches BFS route length:

- (1, 0): 6 moves;
- (7, 6): 10 moves;
- (4, 3): 6 moves.

## My controlled parameter experiments

I train with 50, 500, 2,000 and 10,000 episodes under the same random seed and main parameters. I also vary alpha between 0.10, 0.30 and 0.70 at 2,000 episodes. I distinguish the proportion of training episodes reaching the Goal from the number of final greedy paths that are safely optimal.

## My reproducibility and limitations

My academic notebook needs NumPy, Matplotlib and Python's standard library. It does not require Gym, external CSVs, external APIs or mounting Google Drive. The notebook writes demonstration data and charts to local folders when executed. My results are seed-dependent and demonstrate a deterministic academic grid, not production-ready autonomous driving.

## References

- Muturi, B. (2026). *Assignment 9* [six-slide class PowerPoint], CAI2100C, Miami Dade College.
- Muturi, B. (2026). *Assignment 9 (Q-Learning)* [class notebook].
- Watkins, C. J. C. H., & Dayan, P. (1992). Q-Learning. *Machine Learning, 8*, 279-292. https://doi.org/10.1007/BF00992698
