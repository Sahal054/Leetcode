"""
261. Graph Valid Tree (Graph Theory & Breadth-First Search)

The objective is to determine if a given undirected graph (represented by n nodes 
and a list of edges) is a valid tree. 

In graph theory, a graph is a valid tree if and only if it meets two conditions:
1. It is fully connected (every node can be reached from any other node).
2. It contains exactly zero cycles.

Instead of writing complex cycle-detection logic, this solution leverages a fundamental 
mathematical property of trees: A tree with `n` nodes MUST have exactly `n - 1` edges. 
By checking this first, the problem simplifies dramatically. We only need to use BFS 
to verify that the graph is fully connected.

--- The Core Intuition ---
1. The Mathematical Shortcut: If `len(edges) != n - 1`, it is mathematically impossible 
   for the graph to be a tree. It either has a cycle (too many edges) or is disconnected 
   (too few edges). We return False immediately.
2. Graph Construction: We build an undirected adjacency list `adj` so we can traverse 
   from any node to its connected neighbors.
3. The BFS Traversal: We start a Breadth-First Search from node 0. We use a `queue` to 
   process nodes level by level, and a `visit` set to keep track of seen nodes so we 
   don't process them twice.
4. The Connectivity Check: Once the BFS finishes, the `visit` set contains every node 
   that was reachable from node 0. If `len(visit) == n`, it means the entire graph is a 
   single connected component. Combined with the `n - 1` edge check, it's a guaranteed tree!

--- Visual Traversal Walkthrough ---

Example Graph: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

[ INITIAL SETUP ]
- Edge Check: 4 edges == (5 - 1). It passes the mathematical test.
- Build Adjacency List:
  0: [1, 2, 3]
  1: [0, 4]
  2: [0]
  3: [0]
  4: [1]
- Start BFS at node 0:
  Queue = [0]  |  Visit = {0}

[ ITERATION 1 ]
- Pop 0.
- Neighbors of 0 are [1, 2, 3]. None are in the visit set.
- Add all to Queue and Visit.
  Queue = [1, 2, 3]  |  Visit = {0, 1, 2, 3}

[ ITERATION 2 ]
- Pop 1.
- Neighbors of 1 are [0, 4]. 
- 0 is already visited. 4 is unvisited.
- Add 4 to Queue and Visit.
  Queue = [2, 3, 4]  |  Visit = {0, 1, 2, 3, 4}

[ ITERATIONS 3, 4, 5 ]
- Pop 2: Neighbor 0 is already visited. (Queue = [3, 4])
- Pop 3: Neighbor 0 is already visited. (Queue = [4])
- Pop 4: Neighbor 1 is already visited. (Queue = [])

[ FINAL CHECK ]
- The queue is empty.
- len(visit) is 5.
- Does len(visit) == n (5 == 5)? YES!
Final Return: True

*Note on cycles: If the graph had a cycle (e.g., an edge between 2 and 3), the initial 
`len(edges) != n - 1` check would have caught it and returned False immediately before 
any BFS even started.*

--- Complexity ---
- Time Complexity: O(n). Because we enforce that the graph has exactly n - 1 edges, 
  building the adjacency list takes O(n) time. The BFS processes each of the n nodes 
  and n - 1 edges at most once, which is also O(n).
- Space Complexity: O(n) to store the adjacency list, the BFS queue, and the visit set.
"""

from typing import List
import collections
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges. 
        # If it doesn't, it either has cycles or is disconnected.
        if len(edges) != n - 1:
            return False

        # Build an undirected adjacency list
        adj = collections.defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Initialize BFS structures
        queue = deque()
        visit = set()

        # Start BFS from the first node (node 0)
        queue.append(0)
        visit.add(0)
        
        while queue:
            curr = queue.popleft()
            
            # Explore all neighbors of the current node
            for nei in adj[curr]:
                if nei not in visit:
                    visit.add(nei) 
                    queue.append(nei)

        # If we visited all 'n' nodes, the graph is fully connected.
        # Connected + exactly (n - 1) edges = Valid Tree.
        return len(visit) == n
