"""
433. Minimum Genetic Mutation (Graph & Breadth-First Search) same as word ladder 

The objective is to find the minimum number of mutations to mutate a `startGene` 
into an `endGene`. Each mutation changes exactly one character, and every intermediate 
gene must exist in the `bank`.

This is functionally identical to the "Word Ladder" problem. We use Breadth-First 
Search (BFS) to guarantee the shortest path. 

--- The Core Intuition ---
1. The Setup: We treat this as an unweighted shortest-path graph problem. The genes 
   are the "nodes", and a difference of exactly one character represents an "edge".
2. Wildcard Grouping: Instead of manually comparing every gene to every other gene in 
   the bank to find edges, we use patterns. "AACCGGTT" generates 8 patterns: 
   "*ACCGGTT", "A*CCGGTT", "AA*CGGTT", etc. We group all genes that share a pattern.
3. Graph Traversal: We queue up the `startGene` and perform a level-by-level BFS. 
   For every gene we process, we generate its patterns, look up all connected genes 
   in our adjacency list (`adj`), and add the unvisited ones to the queue.
4. Level Counting: Every time we finish processing all genes currently in the queue 
   (one full level of breadth), we increment our `res` counter.
5. The Exit: If we pop the `endGene` from the queue, we return `res`. If the queue 
   empties entirely, a valid mutation path is impossible, and we return -1.

--- Visual Traversal Walkthrough ---

Example: start = "AACCGGTT", end = "AACCGGTA"
bank = ["AACCGGTA"]

[ PRE-PROCESSING ]
Bank becomes: ["AACCGGTA", "AACCGGTT"]
Build `adj` dictionary:
"AACCGGT*" -> ["AACCGGTA", "AACCGGTT"]
... (and many other patterns)

[ BFS LEVEL 0 ]
- queue = ["AACCGGTT"], visit = {"AACCGGTT"}, res = 0
- Queue size is 1. Pop "AACCGGTT".
- Generate patterns. One of them is "AACCGGT*".
- Neighbors for "AACCGGT*" are ["AACCGGTA", "AACCGGTT"].
- "AACCGGTT" is already visited. Skip.
- "AACCGGTA" is unvisited. Add to `visit` and `queue`.
- Loop finishes. Increment res to 1.

[ BFS LEVEL 1 ]
- queue = ["AACCGGTA"], visit = {"AACCGGTT", "AACCGGTA"}, res = 1
- Pop "AACCGGTA".
- "AACCGGTA" == endGene! Return res (1).

--- Complexity ---
- Time Complexity: $O(N \cdot M^2)$ where $N$ is the size of the bank and $M$ is the 
  length of a gene (which is always 8). Creating the substrings for patterns takes 
  $O(M)$ time, and we do it $M$ times for $N$ words. Because $M$ is bounded to 8, 
  this simplifies to $O(N)$.
- Space Complexity: $O(N \cdot M^2)$ for the `adj` dictionary, storing $N$ genes 
  across $M$ patterns. Again, because $M$ is constant (8), this effectively scales at $O(N)$.
"""

from typing import List
import collections
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # If the target gene is not a valid mutation in the bank, return early
        if endGene not in bank:
            return -1
        
        # Adjacency list mapping wildcard patterns to lists of matching genes
        adj = collections.defaultdict(list)

        # Append startGene so we can build patterns for it to find initial neighbors
        bank.append(startGene)

        # Pre-processing: Build the graph using wildcard patterns
        for gene in bank:
            for i in range(len(gene)):
                # Replace the i-th character with an asterisk to create a pattern
                pattern = gene[:i] + "*" + gene[i+1:]
                adj[pattern].append(gene)

        # Initialize BFS queue and visited set
        queue = deque()
        visit = set()
        
        queue.append(startGene)
        visit.add(startGene)
        
        # Tracks the number of mutations (edges traversed)
        res = 0

        while queue:
            # Process the graph level by level
            for _ in range(len(queue)):
                gene = queue.popleft()

                # If we've reached our destination, return the number of mutations
                if gene == endGene:
                    return res 

                # Re-generate the patterns to look up the neighbors in our adjacency list
                for i in range(len(gene)):
                    pattern = gene[:i] + "*" + gene[i+1:]

                    # Iterate through all valid gene mutations mapped to this pattern
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            
            # Increment mutation count after processing all nodes at the current level
            res += 1
            
        # If the queue empties and endGene was never found, no path exists
        return -1
