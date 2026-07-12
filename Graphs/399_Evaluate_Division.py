"""
399. Evaluate Division (Graph & Breadth-First Search)

The objective is to evaluate a series of division queries (e.g., a / c = ?) based on a 
given set of equations (e.g., a / b = 2.0) and their corresponding values. If a query 
cannot be determined, return -1.0.

Instead of trying to mathematically substitute variables using complex algebraic rules, 
this solution creatively models the problem as a directed, weighted graph. Variables 
become nodes, and the division values become edge weights, reducing the problem to 
standard path-finding using Breadth-First Search (BFS).

--- The Core Intuition ---
1. Graph Construction: We build an adjacency list (`adj`). If equation `A / B = V`, 
   we add a directed edge from `A` to `B` with weight `V`.
2. The Reverse Edge: Crucially, if A / B = V, then by definition, B / A = 1 / V. 
   We add this reverse edge to the graph so we can traverse backwards if needed.
3. Path Accumulation (Multiplication): To evaluate `a / c`, we might need to follow 
   the path `a -> b -> c`. Mathematically, (a / b) * (b / c) = (a / c). Therefore, 
   as we traverse the graph, we MULTIPLY the weights along the path.
4. BFS Traversal: For each query `[src, target]`, we launch a BFS. The queue stores 
   the current node and the cumulative multiplied weight to reach that node. 
5. Impossible Queries: If either the `src` or `target` node doesn't exist in our graph 
   at all, or if the BFS finishes without finding the target, we return -1.

--- Visual Traversal Walkthrough ---

Equations: [["a","b"], ["b","c"]] | Values: [2.0, 3.0]
Query: ["a", "c"]

[ PHASE 1: Graph Construction ]
- a / b = 2.0  ->  adj["a"] appends ["b", 2.0]  | adj["b"] appends ["a", 0.5]
- b / c = 3.0  ->  adj["b"] appends ["c", 3.0]  | adj["c"] appends ["b", 0.33]

[ PHASE 2: Evaluating Query ["a", "c"] ]
- Are both "a" and "c" in the graph? Yes.
- Start BFS from "a".
  Queue: [("a", 1)]  |  Visit: {"a"}

ITERATION 1:
- Pop ("a", 1). Does "a" == target "c"? No.
- Neighbors of "a": 
  -> "b" (weight 2.0). Unvisited! 
  -> Cumulative weight = 1 * 2.0 = 2.0.
  -> Queue: [("b", 2.0)] | Visit: {"a", "b"}

ITERATION 2:
- Pop ("b", 2.0). Does "b" == target "c"? No.
- Neighbors of "b":
  -> "a" (weight 0.5). Already visited! Skip.
  -> "c" (weight 3.0). Unvisited!
  -> Cumulative weight = 2.0 * 3.0 = 6.0.
  -> Queue: [("c", 6.0)] | Visit: {"a", "b", "c"}

ITERATION 3:
- Pop ("c", 6.0). Does "c" == target "c"? YES!
- Return the cumulative weight: 6.0.

Final Result for query ["a", "c"] is 6.0.

--- Complexity ---
- Time Complexity: O(Q * (V + E)) where Q is the number of queries, V is the number of 
  unique variables (nodes), and E is the number of equations (edges). In the worst case, 
  each query might require a full traversal of the graph.
- Space Complexity: O(V + E) to store the adjacency list and the `visit` set/queue 
  during the BFS operations.
"""

from typing import List
import collections
from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Adjacency list for the graph: node -> list of [neighbor, weight]
        adj = collections.defaultdict(list)

        # 1. Build the Graph
        for i, eq in enumerate(equations):
            a, b = eq 
            # A / B = value
            adj[a].append([b, values[i]])
            # B / A = 1 / value
            adj[b].append([a, 1 / values[i]])

        # 2. BFS Helper Function
        def bfs(src, target):
            # If either node is completely unknown to our graph, the answer is impossible
            if src not in adj or target not in adj:
                return -1.0 
                
            queue = deque()
            visit = set()

            # Queue stores [current_node, cumulative_product]
            queue.append([src, 1.0])
            visit.add(src)

            while queue:
                n, w = queue.popleft()
                
                # If we've reached the target node, return the accumulated multiplied weight
                if n == target:
                    return w
                
                # Explore neighbors
                for nei, weight in adj[n]:
                    if nei not in visit:
                        # Multiply the current cumulative weight by the edge weight
                        queue.append([nei, w * weight])
                        visit.add(nei)

            # If the queue empties and we never found the target, they are disconnected
            return -1.0

        # 3. Process all queries
        return [bfs(q[0], q[1]) for q in queries]
