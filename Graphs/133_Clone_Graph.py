"""
133. Clone Graph (Depth-First Search & Hash Map)

The objective is to return a deep copy (clone) of a connected, undirected graph. 
A deep copy means creating entirely new nodes with the same values, rather than 
just returning references to the original nodes.

This solution uses a Depth-First Search (DFS) to traverse the graph and a Hash Map 
to keep track of nodes we have already copied. The Hash Map is crucial for two reasons: 
it prevents infinite loops (since graphs can have cycles), and it ensures that if multiple 
nodes share the same neighbor, they all point to the exact same cloned instance.

--- The Core Intuition ---
1. The Hash Map (`oldToNew`): Maps the original node (key) to its corresponding 
   cloned node (value).
2. The Base Case (Cycle Prevention): Inside the DFS, if we encounter a node that is 
   already in our Hash Map, it means we've already cloned it. We simply return the 
   existing clone rather than creating a new one.
3. Cloning Step: If the node hasn't been visited, we create a new `Node` with the 
   same value as the original. 
4. Mapping Immediately: We immediately add this new clone to the Hash Map BEFORE 
   iterating through its neighbors. This guarantees that if a neighbor loops back 
   to this node, the base case will catch it.
5. Connecting Neighbors: We iterate through the original node's neighbors, recursively 
   call DFS on each, and append the returned cloned neighbors to the new node's 
   `neighbors` list.

--- Visual Traversal Walkthrough ---

Example Graph: Node 1 <---> Node 2 
(Node 1 has neighbor Node 2, Node 2 has neighbor Node 1)

[ INITIAL SETUP ]
- oldToNew = {}
- Start by calling dfs(Node 1)

[ DFS(Node 1) ]
- Is Node 1 in oldToNew? No.
- Create copy: Node 1' (val = 1, neighbors = [])
- Map it: oldToNew = { Node 1: Node 1' }
- Iterate neighbors of Node 1:
  -> Neighbor is Node 2. 
  -> Call dfs(Node 2)

      [ DFS(Node 2) ]
      - Is Node 2 in oldToNew? No.
      - Create copy: Node 2' (val = 2, neighbors = [])
      - Map it: oldToNew = { Node 1: Node 1', Node 2: Node 2' }
      - Iterate neighbors of Node 2:
        -> Neighbor is Node 1.
        -> Call dfs(Node 1)

            [ DFS(Node 1) - CYCLE DETECTED ]
            - Is Node 1 in oldToNew? YES!
            - Return oldToNew[Node 1], which is Node 1'

      - Back in DFS(Node 2): 
        Append the returned Node 1' to Node 2'.neighbors
        Node 2' is now: (val = 2, neighbors = [Node 1'])
      - Return Node 2'

- Back in DFS(Node 1): 
  Append the returned Node 2' to Node 1'.neighbors
  Node 1' is now: (val = 1, neighbors = [Node 2'])
- Return Node 1'

[ FINAL RETURN ]
The initial `dfs(node)` call finishes and returns Node 1', which is fully connected 
to the rest of the deeply copied graph.

--- Complexity ---
- Time Complexity: O(V + E) where V is the number of vertices (nodes) and E is the 
  number of edges. We visit every node exactly once and iterate through every edge 
  to build the new neighbor connections.
- Space Complexity: O(V) to store the `oldToNew` Hash Map, which will contain all V 
  nodes. The DFS recursion call stack will also take O(H) space, where H is the height 
  of the graph (worst case O(V)). Thus, overall space is O(V).
"""

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hash map to map original nodes to their cloned counterparts
        oldToNew = {}

        def dfs(node):
            # Base case: if the node is already cloned, return the clone.
            # This handles cycles and prevents infinite recursion.
            if node in oldToNew:
                return oldToNew[node]
            
            # Create a clone of the current node
            copy = Node(node.val)
            
            # IMMEDIATELY add to the map before traversing neighbors
            oldToNew[node] = copy

            # Recursively clone all neighbors and append them to the copy's list
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            # Return the fully constructed clone
            return copy 
            
        # Handle the edge case of an empty graph
        return dfs(node) if node else None
