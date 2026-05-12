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

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

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

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
| S | S is the starting location for the Torchbearer, so it is the first source node. |
| M | M is a set of relic chamber locations the Torchbearer must visit, so to traverse from one relic chamber to another, each relic chamber visited becomes a source node. |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | 2D hash map |
| What the keys represent | The hash map's keys represent pairs of (source node, destination node). |
| What the values represent | The values represent the minimum fuel cost between the source and destination node. |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | O(1) lookup is possible because hash maps use hash functions to access the memory addresses of the keys, resulting in a quick time complexity of O(1). |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _k + 1 Dijkstra runs, because there are k runs needed to find the shortest fuel cost between the M relic chambers, and then 1 more run to find the shortest fuel cost between the start location S and one of the relic chambers. 
- **Cost per run:** _O(m log n)
- **Total complexity:** _O((k+1) * m log n) = O(k * m log n)
- **Justification (one line):** _There are k + 1 Dijkstra runs that need to be completed, and each run costs O(m log n), so multiplied together the 1 in k + 1 is overlooked as a constant, resulting in O(k * m log n).

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _The invariant holds before each loop, because for nodes already finalized in S, for them to be added to S, the value contained for each node must be the shortest-path distance (by definition). Therefore, before each loop begins, every vertex v contained in S, dist[v] is the true shortest-path distance. 

- **For nodes not yet finalized (not in S):**
  _The invariant holds before each loop, because for nodes not yet finalized in S, each node's dist[] is the current estimate of shortest path distance (by definition). Since the current dist[] is simply an estimate, therefore, at the beginning of each iteration, for nodes not finalized in S, their vertices u and the dist[u] must be the shortest known/estimate distance. 

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Before the first iteration, no true shortest-path distances for any nodes are known because the loop has not iterated yet. Therefore, no nodes are finalized in S yet, and so for every vertex v contained in S, dist[v] is their true shortest-path holds true because there are no vertices in S. Similarly, no true short-path distances are known, so for all other nodes not in S, dist[] merely holds the current known shortest distance for each vertice, and the invariant holds true.

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Finalizing the min-dist node is always correct, because for a node to be finalized in S, the value contained in dist[] must be the true shortest-path distance by definition. For a node's minimum distance to be known, every possible path must be explored, and even though the edge weights can be non-negative, it is essential to explore every path to be able to confidently name a true shortest-path distance. Therefore, finalizing the node when the minimum possible distance cost is known is correct. 

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The invariant guarantees that when the algorithm ends, at the beginning of the next iteration, S will contain all the nodes with true shortest-path distances that are known, and all the other nodes not contained in S will contain the value of the current known shortest distance. Therefore, when the algorithm terminates, the loop contents will not execute, so the invariant remains true.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Connecting correct distances to S allows the Torchbearer to plan ahead and correctly choose the way to traverse the paths using the minimum fuel cost; otherwise, having incorrect "shortest" distances in S could lead to longer paths and running out of fuel. 

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _The failure mode is solely considering locally optimal solutions and where greedy fails is to consider shorter paths that may involve traversing across multiple nodes.
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
