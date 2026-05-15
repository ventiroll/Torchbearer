# Development Log – The Torchbearer

**Student Name:** Mandy Liu
**Student ID:** 129961283

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/10]: Initial Plan

_I plan to implement a 2D hashmap to keep track of the graph and the fuel costs, and multiple (k + 1) Dijkstra's algorithm runs in order to find the total minimum fuel cost to traverse from start to exit location and visiting all relic chambers. I expect coding Dijkstra's and making sure all possible paths are being considered to be difficult, and I plan to test by using my own graph and seeing how my code executes using it.

---

## Entry 2 – [5/11]: Initial Problem Set Up & Coding


_I went in depth into the algorithm's loop invariant and why greedy fails. I also reflected the selecting sources function as well as the precomputing distances, and wrote a function for running Dijkstra's algorithm to eventually find the minimum fuel cost. I decided to use a heap for Dijkstra's to maintain a priority queue and surface the minimum cost closest node, and kept using a 2D hashmap for the vertices' distances.

---

## Entry 3 – [5/12]: Optimal Data Structure Initializing 

_I explored an counterexample of why greedy fails, the components of my search table, and the data structure I have chosen to track what relics have been collected, frozenset. With the choice of using frozenset now, instead of a 2D hashmap for keeping track of the vertices, I am now going to use a hashmap keyed by (node, frozenset) pairs to track true minimum distances.

---

## Entry 4 – [5/14 9 AM]: Post-Implementation Reflection


_I implemented a hashmap with frozenset nodes to keep track of minimum fuel costs. If given more time, I would want to add more tests for duplicate relics or disconnected graphs, or replace the backtracking with bitmask dynamic programming to improve the time complexity for larger graphs.

---

## Final Entry – [5/14 5 PM]: Time Estimate

_I cleaned up my DEVLOG and README, added a few comments to my code, and did some final test runs.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | Half an hour/30 minutes |
| Part 2: Precomputation Design | An hour/60 minutes |
| Part 3: Algorithm Correctness | Half an hour/30 minutes |
| Part 4: Search Design | Half an hour/30 minutes |
| Part 5: State and Search Space | Half an hour/30 minutes |
| Part 6: Pruning | Half an hour/30 minutes |
| Part 7: Implementation | 5 hours/300 minutes |
| README and DEVLOG writing | 1 hour/60 minutes |
| **Total** | ~ 9.5 hours/570 minutes |
