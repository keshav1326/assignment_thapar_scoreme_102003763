
### 2. `main.py`


"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""
from collections import defaultdict, deque


def longest_path(graph: list) -> int:
    # Your implementation goes here
    n = len(graph)
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

    pass

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    n = len(graph)
    in_degree = [0] * n
    adj_list = defaultdict(list)

    # Populate the in-degree and adjacency list
    for u, edges in enumerate(graph):
        for v, w in edges:
            adj_list[u].append((v, w))
            in_degree[v] += 1

    # Perform topological sort
    queue = deque([u for u in range(n) if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v, w in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return topo_order
    pass

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    # Your implementation goes here
    n = len(graph)
    dp = [0] * n
    max_path = 0

    for u in topo_order:
        for v, w in graph[u]:
            dp[v] = max(dp[v], dp[u] + w)
            max_path = max(max_path, dp[v])

    return max_path
    pass
