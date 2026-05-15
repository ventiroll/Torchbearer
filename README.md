# The Torchbearer

**Student Name:** Mandy Liu
**Student ID:** 129961283
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  _A single shortest-path run from S is not enough because each relic chamber in M must be visited once, 
  and the shorter path between two relic chambers can involve going through multiple different chambers.
  A shortest-path run opts to choose a more locally-optimal solution and not consider a globally optimal solution.

- **What decision remains after all inter-location costs are known:**
  _After all inter-location costs are known, the decision to choose what order to connect the locations in to get the total lowest trail fuel cost remains.

- **Why this requires a search over orders (one sentence):**
  _This requires a search over orders, because you must consider all fuel costs and a globally optimal solution in order to find the total lowest trail fuel cost.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
| S | S is the starting location for the Torchbearer, so it is the first source node. |
| M | M is a set of relic chamber locations the Torchbearer must visit, so to traverse from one relic chamber to another, each relic chamber visited becomes a source node. |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | 2D hash map |
| What the keys represent | The hash map's keys represent pairs of (source node, destination node). |
| What the values represent | The values represent the minimum fuel cost between the source and destination node. |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | O(1) lookup is possible because hash maps use hash functions to access the memory addresses of the keys, resulting in a quick time complexity of O(1). |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** _k + 1 Dijkstra runs, because there are k runs needed to find the shortest fuel cost between the M relic chambers, and then 1 more run to find the shortest fuel cost between the start location S and one of the relic chambers. 
- **Cost per run:** _O(m log n)
- **Total complexity:** _O((k+1) * m log n) = O(k * m log n)
- **Justification (one line):** _There are k + 1 Dijkstra runs that need to be completed, and each run costs O(m log n), so multiplied together the 1 in k + 1 is overlooked as a constant, resulting in O(k * m log n).

---

## Part 3: Algorithm Correctness


### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  _The invariant holds before each loop, because for nodes already finalized in S, for them to be added to S, the value contained for each node must be the shortest-path distance (by definition). Therefore, before each loop begins, every vertex v contained in S, dist[v] is the true shortest-path distance. 

- **For nodes not yet finalized (not in S):**
  _The invariant holds before each loop, because for nodes not yet finalized in S, each node's dist[] is the current estimate of shortest path distance (by definition). Since the current dist[] is simply an estimate, therefore, at the beginning of each iteration, for nodes not finalized in S, their vertices u and the dist[u] must be the shortest known/estimate distance. 

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  _Before the first iteration, no true shortest-path distances for any nodes are known because the loop has not iterated yet. Therefore, no nodes are finalized in S yet, and so for every vertex v contained in S, dist[v] is their true shortest-path holds true because there are no vertices in S. Similarly, no true short-path distances are known, so for all other nodes not in S, dist[] merely holds the current known shortest distance for each vertice, and the invariant holds true.

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Finalizing the min-dist node is always correct, because for a node to be finalized in S, the value contained in dist[] must be the true shortest-path distance by definition. For a node's minimum distance to be known, every possible path must be explored, and even though the edge weights can be non-negative, it is essential to explore every path to be able to confidently name a true shortest-path distance. Therefore, finalizing the node when the minimum possible distance cost is known is correct. 

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The invariant guarantees that when the algorithm ends, at the beginning of the next iteration, S will contain all the nodes with true shortest-path distances that are known, and all the other nodes not contained in S will contain the value of the current known shortest distance. Therefore, when the algorithm terminates, the loop contents will not execute, so the invariant remains true.

### Part 3c: Why This Matters for the Route Planner

_Connecting correct distances to S allows the Torchbearer to plan ahead and correctly choose the way to traverse the paths using the minimum fuel cost; otherwise, having incorrect shortest distances in S could lead to longer paths and running out of fuel. 

---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** _The failure mode is solely considering locally optimal solutions and greedy always opts to choose the next nearest unvisited relic chamber, and fails is to consider shorter paths that may involve traversing across multiple further nodes.
- **Counter-example setup:** {S, R1, R2, R3, T} Cost S to R1 is 1, cost S to R2 is 10, cost R1 to R2 is 50, cost R1 to R3 is 2, cost R2 to R3 is 2, cost from any node to exit T is free. 
- **What greedy picks:** _Greedy picks S to R1 (next closest distance of 1), R1 to R3 (next closest distance of 2), R3 to R2 (next closest distance of 50), then to T for a total cost of 53. 
- **What optimal picks:** _Optimal picks S to R2 (cost of 10), R2 to R3 (cost of 2), R3 to R1 (cost of 1), then to T for a total cost of 13. 
- **Why greedy loses:** Greedy loses because it does not consider the total fuel cost of traversing all the relic chambers, and chose the path with the largest cost of 50. Picking an more optimal solution requires backtracking and keeping all the costs in mind.

### What the Algorithm Must Explore


- _The algorithm must explore the order in which the Torchbearer will traverse from the start, every relic chamber, and the exit to get the minimum possible torch cost.

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | currNode | node | Current location of the Torchbearer |
| Relics already collected | visited | frozenset[node] | Unmodifiable set to keep track of locations already visited |
| Fuel cost so far | fuelCost | int | Total cost of fuel cost spent by the Torchbearer traveling |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | frozenset |
| Operation: check if relic already collected | Time complexity: O(1), hash-based search |
| Operation: mark a relic as collected | Time complexity: O(k), creates a new frozenset when new relic is collected |
| Operation: unmark a relic (backtrack) | Time complexity: O(k), backtracking returns to previous frozenset and makes new one |
| Why this structure fits | frozenset fits because its every state is self-contained and hashable, so searching for a collected relic is easy with O(1), and backtracking and marking as collected is simple with creating a new frozenset. |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** _k!
- **Why:** _Starting from the beginning, any of the k relic chambers can be visited, creating k choices for the Torchbearer, then k - 1 choices for the next relic chamber, and so forth, leading to k!.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking


- **What is tracked:** _fuelCost, the currently known accumulated minimum total fuel cost spent by Torchbearer, is being tracked. 
- **When it is used:** _With each recursive call, fuelCost is compared against the current cost, to see if there is a more optimal path to take with a smaller total fuel cost.
- **What it allows the algorithm to skip:** _It allows the algorithm to skip any paths who have a bigger fuel cost than the currently known minimum cost, because any path with a bigger cost is not optimal.

### Part 6b: Lower Bound Estimation


- **What information is available at the current state:** The Torchbearer's current location, the currently known accumulated minimum fuel cost, the set of unvisited relic chambers, and the set of shortest distances between two locations are all known at the current state.
- **What the lower bound accounts for:** _The lower bound accounts for the minimum cost from the Torchbearer's current location to the exit, while traversing all the unvisited relics in between. 
- **Why it never overestimates:** _It never overestimates because it operates based on using the known pre-computed minimum costs of all the paths, so the total path cost cannot be smaller than the individual costs. 

### Part 6c: Pruning Correctness


- _Pruning is safe because the lower bound never overestimates the remaining cost, and only opts to find the minimum total fuel cost, so the optimal solution survives. 
- _The optimal solution will not be cut because the algorithm searches for a complete path with the minimum cost unless a smaller one is found, so the optimal solution will be fully explored always and not trigger the pruning. 

---

## References

- _Lecture notes 
- GeeksforGeeks. (2026, January 21). Dijkstra's algorithm. https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/
