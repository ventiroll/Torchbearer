"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Mandy Liu
Student ID:   129961283

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return "A single shortest-path run from S is not enough because each relic chamber in M must be visited once, and the shorter path between two relic chambers can involve going through multiple different chambers. A shortest-path run opts to choose a more locally-optimal solution and not consider a globally optimal solution. After all inter-location costs are known, the decision to choose what order to connect the locations in to get the total lowest trail fuel cost remains. This requires a search over orders, because you must consider all fuel costs and a globally optimal solution in order to find the total lowest trail fuel cost."


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    return list({spawn, *relics})


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        cost, u = heapq.heappop(heap)
        if cost > dist[u]:
            continue
        for v, weight in graph.get(u, []):
            new_cost = cost + weight
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    return {source: run_dijkstra(graph, source) for source in sources}


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    partA = "The invariant holds before each loop, because for nodes already finalized in S, for them to be added to S, the value contained for each node must be the shortest-path distance (by definition). Therefore, before each loop begins, every vertex v contained in S, dist[v] is the true shortest-path distance. The invariant holds before each loop, because for nodes not yet finalized in S, each node's dist[] is the current estimate of shortest path distance (by definition). Since the current dist[] is simply an estimate, therefore, at the beginning of each iteration, for nodes not finalized in S, their vertices u and the dist[u] must be the shortest known/estimate distance."
    partB = "Before the first iteration, no true shortest-path distances for any nodes are known because the loop has not iterated yet. Therefore, no nodes are finalized in S yet, and so for every vertex v contained in S, dist[v] is their true shortest-path holds true because there are no vertices in S. Similarly, no true short-path distances are known, so for all other nodes not in S, dist[] merely holds the current known shortest distance for each vertice, and the invariant holds true. Finalizing the min-dist node is always correct, because for a node to be finalized in S, the value contained in dist[] must be the true shortest-path distance by definition. For a node's minimum distance to be known, every possible path must be explored, and even though the edge weights can be non-negative, it is essential to explore every path to be able to confidently name a true shortest-path distance. Therefore, finalizing the node when the minimum possible distance cost is known is correct. The invariant guarantees that when the algorithm ends, at the beginning of the next iteration, S will contain all the nodes with true shortest-path distances that are known, and all the other nodes not contained in S will contain the value of the current known shortest distance. Therefore, when the algorithm terminates, the loop contents will not execute, so the invariant remains true."
    partC = "Connecting correct distances to S allows the Torchbearer to plan ahead and correctly choose the way to traverse the paths using the minimum fuel cost; otherwise, having incorrect shortest distances in S could lead to longer paths and running out of fuel."
    return " ".join([partA, partB, partC])


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    part4 = "- **The failure mode:** _The failure mode is solely considering locally optimal solutions and greedy always opts to choose the next nearest unvisited relic chamber, and fails is to consider shorter paths that may involve traversing across multiple further nodes. - **Counter-example setup:** {S, R1, R2, R3, T} Cost S to R1 is 1, cost S to R2 is 10, cost R1 to R2 is 50, cost R1 to R3 is 2, cost R2 to R3 is 2, cost from any node to exit T is free. - **What greedy picks:** _Greedy picks S to R1 (next closest distance of 1), R1 to R3 (next closest distance of 2), R3 to R2 (next closest distance of 50), then to T for a total cost of 53. - **What optimal picks:** _Optimal picks S to R2 (cost of 10), R2 to R3 (cost of 2), R3 to R1 (cost of 1), then to T for a total cost of 13. - **Why greedy loses:** Greedy loses because it does not consider the total fuel cost of traversing all the relic chambers, and chose the path with the largest cost of 50. Picking an more optimal solution requires backtracking and keeping all the costs in mind. The algorithm must explore the order in which the Torchbearer will traverse from the start, every relic chamber, and the exit to get the minimum possible torch cost."
    return part4


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    best = [float('inf'), []]
    relics_remaining = frozenset(relics)
    _explore(dist_table, spawn, relics_remaining, [], 0, exit_node, best)
    return (best[0], best[1])


def _explore(dist_table, currNode, relics_remaining, relics_visited_order,
             fuelCost, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    
    if fuelCost >= best[0]: # pruning, abandon if worse than best found 
        return

    if relics_remaining: # estimating lower bound
        min_out = min(
            dist_table[currNode].get(r, float('inf'))
            for r in relics_remaining
        )
        min_to_exit = min(
            dist_table[r].get(exit_node, float('inf'))
            for r in relics_remaining
        )
        lower_bound = min_out + min_to_exit
        if fuelCost + lower_bound >= best[0]:
            return

    if not relics_remaining: # base case: if all relics collected, then head to exit 
        total = fuelCost + dist_table[currNode].get(exit_node, float('inf'))
        if total < best[0]:
            best[0] = total
            best[1] = list(relics_visited_order)
        return

    for relic in relics_remaining: # recursive: try remaining relics 
        edge_cost = dist_table[currNode].get(relic, float('inf'))
        if edge_cost == float('inf'):
            continue

        # Move to relic
        relics_visited_order.append(relic)
        visited = relics_remaining - {relic}

        _explore(
            dist_table,
            relic,                  # currNode
            visited,                # relics_remaining
            relics_visited_order,
            fuelCost + edge_cost,   # fuelCost
            exit_node,
            best
        )

        relics_visited_order.pop() # backtracking


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
