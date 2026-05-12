# Development Log – The Torchbearer

**Student Name:** Mandy Liu
**Student ID:** 129961283

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/10]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_I plan to implement a 2D hashmap to keep track of the graph and the fuel costs, and multiple (k + 1) Dijkstra's algorithm runs in order to find the total minimum fuel cost to traverse from start to exit location and visiting all relic chambers. I expect coding Dijkstra's and making sure all possible paths are being considered to be difficult, and I plan to test by using my own graph and seeing how my code executes using it.

---

## Entry 2 – [5/11]: Initial Problem Set Up & Coding

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_I went in depth into the algorithm's loop invariant and why greedy fails. I also reflected the selecting sources function as well as the precomputing distances, and wrote a function for running Dijkstra's algorithm to eventually find the minimum fuel cost. I decided to use a heap for Dijkstra's to maintain a priority queue and surface the minimum cost closest node, and kept using a 2D hashmap for the vertices' distances.

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
