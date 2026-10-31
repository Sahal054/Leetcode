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

"""
200. Number of Islands (Depth-First Search / Graph Traversal)

--- The Core Intuition ---
1. The Discovery (Outer Loop): We scan the grid reading it like a book, from top-left 
   to bottom-right. The moment we spot a piece of land (`"1"`) that we haven't seen 
   before, we know we have discovered a brand-new island! We increment our island counter.
2. The Exploration (DFS): Once a new island is found, we must map out its entire 
   landmass so we don't accidentally count its other half as a separate island later. 
   The DFS function acts as an explorer, recursively running as far as it can in all 
   4 directions, marking every connected piece of land as `visited`.
3. The Base Cases (The Boundaries): Our DFS explorer blindly steps in every direction. 
   It only stops and turns back if:
   - It walks off the edge of the map (out of bounds).
   - It steps into the water (`!= "1"`).
   - It walks in a circle and steps on land it has already mapped (`in visit`).
4. The Visited Set: Keeping track of visited coordinates guarantees we only launch our 
   DFS exactly once per island, preventing infinite recursive loops.

--- Visual Traversal Walkthrough ---

Example Grid:
[1, 1, 0]
[1, 0, 0]
[0, 0, 1]

[ INITIAL SETUP ]
- res = 0
- visit = set()
- Scan begins at (0, 0).

[ DISCOVERING ISLAND 1 ]
- (0, 0) is "1" and not visited.
- A new island! res += 1 (res is now 1).
- Launch DFS(0, 0):
  - Mark (0, 0) as visited.
  - Step Down to (1, 0): It's a "1"! Mark visited.
    - (1, 0) steps Right to (1, 1): Water ("0"). Turns back.
    - (1, 0) steps Down to (2, 0): Water ("0"). Turns back.
  - Step Right to (0, 1): It's a "1"! Mark visited.
    - (0, 1) steps Right to (0, 2): Water ("0"). Turns back.
- DFS finishes. The entire top-left landmass is mapped in `visit`.

[ CONTINUING THE SCAN ]
- (0, 1) is "1", but it IS in `visit`. Skip.
- (1, 0) is "1", but it IS in `visit`. Skip.
- All "0"s are skipped.

[ DISCOVERING ISLAND 2 ]
- (2, 2) is "1" and not in `visit`.
- A new island! res += 1 (res is now 2).
- Launch DFS(2, 2):
  - Mark (2, 2) as visited.
  - All 4 directions lead off the map or to water. DFS finishes instantly.

[ END ]
- Grid scan finishes. Return res (2).

--- Complexity ---
- Time Complexity: $O(M \times N)$ where $M$ is rows and $N$ is columns. Even with the 
  nested loops and recursion, every single cell is evaluated and marked as visited 
  at most a constant number of times. 
- Space Complexity: $O(M \times N)$. In the absolute worst-case scenario (where the 
  entire grid is one giant landmass), the recursive call stack will go $M \times N$ 
  levels deep. The `visit` set also scales up to $M \times N$ size.
"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        res = 0
        
        # Tracks coordinates we've already mapped so we don't count them twice
        visit = set()
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # BASE CASES: Stop exploring if we hit boundaries, water, or mapped land
            if (r not in range(rows) or 
                c not in range(cols) or
                grid[r][c] != "1" or 
                (r, c) in visit):
                return
            
            # Mark the current piece of land as mapped
            visit.add((r, c))

            # Recursively explore all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        # The Grid Scan (Outer Loop)
        for r in range(rows):
            for c in range(cols):
                
                # If we find land we haven't mapped yet, we found a new island
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)  # Map out its entire connected landmass
                    res += 1   # Increment our total island count
                    
        return res
