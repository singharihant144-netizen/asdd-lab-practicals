# AISC Viva Questions and Short Answers

These questions are based on the nine supplied AISC notebooks. No external dataset was included.


## AISC-01 — 8 puzzle

**Q01. What is the state representation in the 8-puzzle solver?**

A board is flattened into a tuple of nine values, with 0 representing the blank tile.

**Q02. What is the Manhattan-distance heuristic?**

It sums each numbered tile’s row and column distance from its goal position, excluding the blank.

**Q03. Why is A* search optimal with an admissible heuristic?**

With an admissible heuristic and correct A* bookkeeping, the first optimal goal path has minimum cost.

**Q04. What does the priority queue store?**

It orders candidate states by accumulated path cost plus estimated remaining cost.

**Q05. Why must the solver avoid revisiting states?**

A visited or best-cost map prevents repeated work and cycles while retaining improved paths.

## AISC-02 — AND gate

**Q01. What is a perceptron?**

A perceptron computes a weighted sum and applies an activation function to produce a class.

**Q02. How does the step activation function classify an input?**

The step function maps the net input to binary output according to a threshold.

**Q03. What is the role of the bias?**

Bias shifts the decision threshold independently of the input features.

**Q04. How does the perceptron learning rule update weights?**

It adjusts weights and bias in proportion to learning rate, error, and the input.

**Q05. Why does an AND gate converge with a single perceptron?**

AND is linearly separable, so one linear decision boundary can separate its positive case.

## AISC-03 — BFS

**Q01. How does breadth-first search explore a graph?**

It visits nodes layer by layer, exploring all nearer nodes before deeper ones.

**Q02. Why does BFS use a queue?**

A FIFO queue preserves the order in which frontier nodes were discovered.

**Q03. When does BFS find a shortest path?**

In an unweighted graph, BFS finds a shortest path when it first reaches the goal.

**Q04. Why keep a visited set?**

It prevents cycles and repeated expansion of already explored nodes.

**Q05. What is the time complexity of BFS?**

With adjacency lists, time is O(V+E) and space is O(V).

## AISC-04 — DFS

**Q01. How does depth-first search explore a graph?**

It follows one branch as far as possible, then backtracks to another branch.

**Q02. How does recursion represent the DFS stack?**

Each recursive call keeps the current node on the call stack until its descendants finish.

**Q03. Why track visited nodes?**

The set prevents cycles and duplicate exploration.

**Q04. Does DFS guarantee the shortest path?**

No. DFS may find a longer path before a shorter one.

**Q05. What is the time complexity of DFS?**

With adjacency lists, time is O(V+E), with O(V) auxiliary space.

## AISC-05 — min-max algorithm for tic-tac-toe

**Q01. What is the Minimax algorithm?**

It searches possible future moves assuming both players choose optimally.

**Q02. What do maximizing and minimizing players represent?**

The maximizing player seeks the highest score; the opponent is modeled as minimizing it.

**Q03. How is a terminal board scored?**

Wins, losses, and draws receive utility values that rank outcomes.

**Q04. Why does Minimax choose the best move under optimal play?**

It evaluates each available move against the opponent’s best response.

**Q05. What is the main cost of plain Minimax?**

The game tree grows exponentially with search depth; pruning can reduce explored nodes.

## AISC-06 — OR gate

**Q01. What output does an OR gate produce?**

It returns 1 when at least one binary input is 1; otherwise it returns 0.

**Q02. How does a perceptron learn the OR truth table?**

Training compares each prediction to its label and nudges weights and bias by the error.

**Q03. What do weights represent in this model?**

Weights determine how strongly each input contributes to the net activation.

**Q04. Why is a bias needed?**

Bias shifts the threshold so the desired boundary can be represented.

**Q05. What is a limitation of a hard-threshold perceptron?**

A hard threshold is not differentiable and a single perceptron cannot model non-linearly separable patterns.

## AISC-07 — Supervised Neural Network Perceptron

**Q01. What makes learning supervised?**

The training examples include target labels that guide parameter updates.

**Q02. What are the input features and labels in this experiment?**

The two binary inputs are features and the provided y array contains target labels.

**Q03. How is prediction error used to update the model?**

The label minus prediction error scales the weight and bias corrections.

**Q04. What does the learning rate control?**

It controls the size of each update and therefore the speed and stability of learning.

**Q05. How can you check whether the trained perceptron learned the target?**

Run predictions on all training rows and compare them with the target labels; also inspect held-out data for generalization.

## AISC-08 — Unsupervised Neural Network HEBBIAN

**Q01. What is unsupervised learning?**

It learns patterns from input structure without target labels.

**Q02. What is the basic Hebbian learning principle?**

The classic rule strengthens a connection when its input and output activity co-occur.

**Q03. How does this code update its weight vector?**

For each vector x, it computes y=w·x and updates w by learning_rate times y times x.

**Q04. What does the output dot product represent here?**

It is the scalar activation produced by the current weights and input vector.

**Q05. Why can this simple Hebbian update become numerically unstable?**

Repeated unnormalized updates can grow weights rapidly, so normalization or smaller rates may be needed.

## AISC-09 — XOR gate

**Q01. Why can a single perceptron not represent XOR?**

XOR is not linearly separable, so a single linear threshold cannot classify it.

**Q02. What role does the hidden layer play in this network?**

Hidden units learn intermediate nonlinear features that enable a nonlinear decision boundary.

**Q03. What does the sigmoid function provide?**

Sigmoid maps real-valued activations smoothly into the interval from 0 to 1.

**Q04. Why does backpropagation use derivatives?**

The chain rule computes how each parameter contributed to the output error.

**Q05. How would you check that the trained network learned XOR?**

Predict the four input combinations and verify outputs are close to 0, 1, 1, 0 after thresholding.
