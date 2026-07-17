"""
695. Max Area of Island (Depth-First Search)

The objective is to find the maximum area of an island in a given 2D grid. 
An island is surrounded by water (0s) and is formed by connecting adjacent lands (1s) 
horizontally or vertically. The area of an island is the total number of cells with a 1 in it.

This solution iterates through every cell in the grid. When it finds unvisited land, 
it uses a Depth-First Search (DFS) to explore the entire island. The DFS recursively 
counts the number of connected land cells and returns the total area. We keep track 
of the maximum area found across all islands.

--- The Core Intuition ---
1. Global Scan: We check every `(r, c)` coordinate in the grid using nested loops.
2. The DFS Function: When called on a coordinate, it calculates the area of the 
   connected land starting from that point. 
3. Base Cases (Stopping Conditions): If the recursive search goes out of the grid boundaries, 
   hits water (0), or hits a cell we've already visited, it contributes an area of 0.
4. Recursive Accumulation: If a cell is valid unvisited land, we mark it as visited. 
   Its total area is `1` (itself) PLUS the areas of land adjacent to it 
   (Up, Down, Left, Right).
   Formula: 1 + dfs(Up) + dfs(Down) + dfs(Left) + dfs(Right)
5. Max Tracking: As we scan the grid, we constantly update our `area` variable to 
   store the maximum value between the current `area` and the result of the new `dfs`.

--- Visual Traversal Walkthrough ---

Example Grid:
  0 1 2
0 1 1 0
1 0 1 0
2 0 0 1

[ OUTER LOOP STARTS ]

-> r=0, c=0: Found "1" and unvisited!
   Run DFS(0, 0):
   - Mark (0,0) visited.
   - Area = 1 + dfs(1,0) + dfs(-1,0) + dfs(0,1) + dfs(0,-1)
     - dfs(1,0): Hits "0" (water). Returns 0.
     - dfs(-1,0): Out of bounds. Returns 0.
     - dfs(0,1): Valid land! Mark (0,1) visited.
       - Area of (0,1) = 1 + dfs(1,1) + dfs(-1,1) + dfs(0,2) + dfs(0,0)
         - dfs(1,1): Valid land! Mark (1,1) visited.
           - Area of (1,1) = 1 + 0 + 0 + 0 + 0 = 1. (Returns 1)
         - dfs(-1,1): Out of bounds. Returns 0.
         - dfs(0,2): Hits "0". Returns 0.
         - dfs(0,0): Already visited! Returns 0.
       - Total for (0,1) = 1 + 1 + 0 + 0 + 0 = 2. (Returns 2)
     - dfs(0,-1): Out of bounds. Returns 0.
   - Total for (0,0) = 1 + 0 + 0 + 2 + 0 = 3. 
   
   area = max(0, 3) -> area becomes 3.

-> r=0, c=1: Already in `visit` set. dfs(0,1) immediately returns 0.
-> r=0, c=2: Hits "0" (water). dfs(0,2) returns 0.
-> ... (skips water and visited cells) ...

-> r=2, c=2: Found "1" and unvisited!
   Run DFS(2, 2):
   - Mark (2,2) visited.
   - Area = 1 + 0 (Up) + 0 (Down) + 0 (Left) + 0 (Right) = 1.
   
   area = max(3, 1) -> area remains 3.

[ OUTER LOOP FINISHES ]
Final Return: 3

--- Complexity ---
- Time Complexity: O(R * C) where R is the number of rows and C is the number of columns. 
  Each cell is visited a constant number of times (once in the outer loop, and bounded 
  times in DFS recursion).
- Space Complexity: O(R * C) in the worst case (a grid entirely filled with "1"s). This 
  space is used by the `visit` hash set and the DFS recursion call stack.
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # Set to keep track of coordinates we have already processed
        visit = set()
        
        area = 0

        def dfs(r, c):
            # Base cases: out of bounds, hit water (0), or already visited
            if (r < 0 or r == ROWS or c == COLS or c < 0 or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            # Mark current land cell as visited
            visit.add((r, c))

            # The area of this land block is 1 (current cell) plus the area of neighbors
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1)) 

        # Iterate through every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # Update max area (if cell is water or visited, dfs returns 0)
                area = max(area, dfs(r, c))

        return area





"""  
THE BFS SOLUTION
"""

import collections
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        max_area = 0

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            visit.add((r, c))
            current_area = 0

            while queue:
                row, col = queue.popleft()
                current_area += 1 # We popped a piece of land, increase the size!
                
                # Check all 4 neighbors
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    # If neighbor is in bounds, is land, and hasn't been visited
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == 1 and (nr, nc) not in visit):
                        
                        queue.append((nr, nc))
                        visit.add((nr, nc)) # Mark visited IMMEDIATELY when adding to queue
            
            return current_area

        # Iterate through every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, bfs(r, c))

        return max_area
