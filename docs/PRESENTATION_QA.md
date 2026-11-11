# My Assignment 9: classroom questions and answers

**Juan Luna Santibanez | Miami Dade College | CAI2100C-2267-6908 | Professor Beth Muturi**

I use these 33 answers to explain my actual implementation in first person.

### 1. What did Professor Muturi ask me to build?

I use reinforcement learning to navigate the official Cliff grid safely, show the shortest route from each of three specified starts, and study parameter changes.

### 2. Which source notebook do I follow?

I use the supplied Assignment 9 (Q-Learning) notebook as my technical reference. I do not treat the optional Gym notebook as a second required submission.

### 3. Why is the official grid different from the example?

The reference demonstrates 5 by 6 cells. I implement the assignment slide's actual 8 by 8 grid.

### 4. Which starting locations do I evaluate?

I use (1, 0), (7, 6) and (4, 3). Each coordinate is written as (row, column) with zero-based indexing.

### 5. Where is the Goal?

I verified that the Goal occupies row 1, column 4.

### 6. How many Cliffs did I encode?

I counted 22 Cliffs and asserted that number in my code.

### 7. What is the agent's state?

I represent its location as a row and column pair on the grid.

### 8. Which actions are allowed?

I permit up, right, down and left as long as the move stays inside the eight-by-eight board.

### 9. What rewards did I choose?

I assign +100 to the Goal, -100 to a Cliff and -1 to each ordinary move to favor shorter safe journeys.

### 10. When does an episode stop?

I stop after reaching the Goal, entering a Cliff or exhausting the allowed step budget.

### 11. What is the Q-table?

I store a learned estimated return for every valid state-action combination in an 8 by 8 by 4 NumPy array.

### 12. What does Q-Learning update?

I update an action value using its observed reward and the best estimated value at the next nonterminal state.

### 13. What is alpha?

Alpha is the learning rate that controls how strongly each experience updates my previous Q-value estimate.

### 14. What is gamma?

Gamma discounts the contribution of future rewards in the update.

### 15. What does epsilon mean in my implementation?

I interpret epsilon as the chance to try a random legal action instead of exploiting the current Q-table.

### 16. Where do I begin training episodes?

I sample safe cells and regularly revisit the three required starting states; I do not feed BFS solutions to the learner.

### 17. Why did I choose a fixed random seed?

Seed 2026 makes my chosen parameter comparisons reproducible; it does not guarantee success for all seeds.

### 18. What is one training episode?

It is one complete attempt from a sampled start until termination or the step limit.

### 19. What happens from (1, 0)?

My learned policy reaches the Goal in six adjacent safe moves, matching the independent BFS distance.

### 20. What happens from (7, 6)?

My learned policy reaches the Goal in ten adjacent safe moves, matching BFS.

### 21. What happens from (4, 3)?

My learned policy reaches the Goal in six adjacent safe moves, matching BFS.

### 22. How do I verify a shortest route?

I independently apply breadth-first search to the legal grid and check that the learned safe path has the same minimum length.

### 23. Does BFS train my model?

No. I use BFS only as an independent acceptance check after learning.

### 24. What did 50 episodes demonstrate?

For my fixed seed and configuration, only one of the three starting positions had an optimal safe greedy path.

### 25. What did 500 and 2,000 episodes demonstrate?

Under the same fixed seed, both training budgets gave all three optimal safe routes.

### 26. Why train a final 10,000-episode model?

I use more experience for a stable classroom demonstration, without asserting a general theorem of safety.

### 27. How do I know the route was not hardcoded?

My training function uses rewards and transitions, not the BFS routes. I inspect the learned greedy policy afterward.

### 28. Is reaching the Goal sufficient to show optimality?

No. I also verify safety, adjacent legal moves and the shortest movement count.

### 29. Does the agent ever enter a Cliff during training?

It can, because exploratory failures teach a negative reward. My evaluated final routes do not enter any Cliff.

### 30. Would this operate a real autonomous vehicle?

No. Real driving involves uncertain dynamics, sensors, human safety and validation well beyond this deterministic grid.

### 31. Why did I produce multiple charts?

I use route figures to inspect behavior and episode, reward and Q-value charts to explain the learning process.

### 32. What is my main finding?

My tabular learner found the three required shortest safe paths, and I distinguished arrival, safety, optimality and training success rate.

### 33. What file should I submit?

I submit my one academic Q-Learning notebook and check Canvas for any group or presentation requirement. My web demo is a supplemental portfolio.
