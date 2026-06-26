"""
200. Number of Islands (Breadth-First Search)

The objective is to count the number of islands in a given 2D grid. An island is 
surrounded by water ("0") and is formed by connecting adjacent lands ("1") horizontally 
or vertically. 

This solution iterates through every cell in the grid. When it finds a piece of unvisited 
land ("1"), it increments the island count and launches a Breadth-First Search (BFS) 
to explore and mark the entire connected island as "visited". This ensures we don't 
count the same island twice.

--- The Core Intuition ---
1. Outer Loop: Scan the grid row by row, column by column.
2. Trigger Condition: If we find a "1" that is NOT in our `visit` set, we have discovered 
   a brand new island.
3. BFS Expansion: From that newly discovered land, use a queue to explore all 4 adjacent 
   directions (up, down, left, right). If a neighbor is also a "1" and unvisited, add it 
   to the queue and mark it visited.
4. Completion: Once the queue is empty, the entire island has been mapped. The outer loop 
   then continues searching for the next unvisited "1".

--- Visual Traversal Walkthrough ---

Example Grid:
  0 1 2
0 1 1 0
1 1 0 0
2 0 0 1

[ OUTER LOOP STARTS ]

-> r=0, c=0: Found "1" and unvisited!
   islands = 1
   Run BFS(0, 0):
   - Queue: [(0,0)] | Visit: {(0,0)}
   - Pop (0,0). Look in 4 directions. 
     Found valid adjacent land at Right (0,1) and Down (1,0).
   - Queue: [(0,1), (1,0)] | Visit: {(0,0), (0,1), (1,0)}
   - Pop (0,1). No unvisited adjacent land.
   - Pop (1,0). No unvisited adjacent land.
   - Queue is empty. Island 1 is fully mapped.

-> r=0, c=1: Found "1", but it is IN the visit set. Skip.
-> r=0, c=2: Found "0". Skip.
-> r=1, c=0: Found "1", but it is IN the visit set. Skip.
-> r=1, c=1: Found "0". Skip.
-> r=1, c=2: Found "0". Skip.
-> r=2, c=0: Found "0". Skip.
-> r=2, c=1: Found "0". Skip.

-> r=2, c=2: Found "1" and unvisited!
   islands = 2
   Run BFS(2, 2):
   - Queue: [(2,2)] | Visit: {..., (2,2)}
   - Pop (2,2). Look in 4 directions. 
     No unvisited adjacent land.
   - Queue is empty. Island 2 is fully mapped.

[ OUTER LOOP FINISHES ]
Final Return: 2

--- Complexity ---
- Time Complexity: O(R * C) where R is rows and C is columns. Every cell is processed 
  by the outer loops, and each cell is added to/popped from the BFS queue at most once.
- Space Complexity: O(R * C) in the worst case (a grid entirely filled with "1"s) to store 
  the nodes in the `visit` set and the BFS `queue`. 
  
  *Note on optimization: In Python, using `queue.pop(0)` on a standard list takes O(N) time. 
  For strict O(1) pops, it is standard practice to import and use `collections.deque` instead 
  of a standard list `[]` for the queue.*
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
             return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            queue = []
            visit.add((r,c))
            queue.append((r,c))

            while queue:
                row,col = queue.pop(0)
                directions =[[1,0],[0,1],[-1,0],[0,-1]]
                for dr ,dc in directions:
                    r,c = row+dr,col+dc

                    if  ((r in range(ROWS)) and 
                         (c in range(COLS)) and
                         grid[r][c] == "1" and
                        (r,c) not in visit):

                        queue.append((r,c))
                        visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands +=1
        return islands
