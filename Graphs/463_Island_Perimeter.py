"""
463. Island Perimeter (Graph & Depth-First Search)

The objective is to calculate the perimeter of a single island within a 2D grid. 
The grid consists of 1s (land) and 0s (water). The perimeter is defined as the 
total number of edges separating land from water or the outer boundary of the grid.

This solution uses Depth-First Search (DFS) to traverse the island. The genius 
of this approach lies in how it defines a "perimeter edge". Instead of looking 
at the whole grid, we stand on a land cell and look in all four directions.

--- The Core Intuition ---
1. What makes a perimeter? If you are standing on a piece of land, a perimeter 
   edge exists if you step off that land and fall into water (0), or if you walk 
   off the edge of the map (out of bounds). In these cases, we add 1 to the perimeter.
2. Internal Edges: If you step from one land cell to another, that boundary is internal 
   and does not count toward the outer perimeter. If the neighboring land is already in 
   our `visit` set, we return 0 for that direction.
3. DFS Traversal: Once we hit a piece of land, the DFS recursively checks top, bottom, 
   left, and right. It adds up the 1s (boundaries/water) and 0s (internal connections) 
   and bubbles that sum back up the call stack.
4. The Global Loop: The loop iterates through every cell and updates `perim` with the 
   maximum value returned by the DFS. (Note: Because water cells immediately trigger the 
   base case and return 1, the `max` function ensures that when we finally hit the actual 
   island and return its full perimeter, it overrides the 1s).

--- Visual Traversal Walkthrough ---

Example Grid: 
[ 1, 0 ]
[ 1, 1 ]

[ INITIAL SETUP ]
ROWS = 2, COLS = 2
visit = set(), perim = 0

[ THE LOOP STARTS ]
- r = 0, c = 0 (Grid[0][0] is 1 - Land!)
-> Run DFS(0, 0):
   - Add (0, 0) to visit.
   - Check Down (1, 0): Land! 
     -> Run DFS(1, 0):
        - Add (1, 0) to visit.
        - Check Down (2, 0): Out of bounds -> Returns 1
        - Check Up (0, 0): In `visit` set -> Returns 0
        - Check Right (1, 1): Land! 
          -> Run DFS(1, 1):
             - Add (1, 1) to visit.
             - Check Down (2, 1): Out of bounds -> Returns 1
             - Check Up (0, 1): Water (0) -> Returns 1
             - Check Right (1, 2): Out of bounds -> Returns 1
             - Check Left (1, 0): In `visit` set -> Returns 0
             - DFS(1, 1) Total = 1 + 1 + 1 + 0 = 3. Returns 3.
        - Check Left (1, -1): Out of bounds -> Returns 1
        - DFS(1, 0) Total = 1 + 0 + 3 + 1 = 5. Returns 5.
   - Check Up (-1, 0): Out of bounds -> Returns 1
   - Check Right (0, 1): Water (0) -> Returns 1
   - Check Left (0, -1): Out of bounds -> Returns 1
   - DFS(0, 0) Total = 5 (from down) + 1 + 1 + 1 = 8. Returns 8.

- perim becomes max(0, 8) = 8.

(The loop continues for the other cells. When DFS is called on water at (0,1), 
it instantly returns 1. perim = max(8, 1) remains 8. Same for already visited 
land cells which return 0).

Final Return: 8

--- Complexity ---
- Time Complexity: O(R * C) where R is the number of rows and C is the number of 
  columns. We iterate through every cell in the grid, and the DFS visits each land 
  cell at most once (checking its 4 neighbors).
- Space Complexity: O(R * C) in the worst-case scenario (if the entire grid is a 
  single massive island). The `visit` set will store every cell, and the DFS recursion 
  call stack will go as deep as the number of land cells.
"""

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        perim = 0

        def dfs(r, c):
            # BASE CASE 1: Out of bounds or water. 
            # This represents an edge of the island, so we count it as 1 perimeter edge.
            if (r == ROWS or c == COLS or r < 0 or c < 0 or grid[r][c] == 0):
                return 1
            
            # BASE CASE 2: Already visited land cell.
            # This represents an internal boundary between two land masses. Counts as 0.
            if (r, c) in visit:
                return 0
            
            # Mark the current land cell as visited so we don't count it again or loop infinitely.
            visit.add((r, c))

            # Recursively check all 4 adjacent directions and sum up their returned perimeter edges.
            return (dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))

        # Iterate over the entire grid to ensure we find the island.
        for r in range(ROWS):
            for c in range(COLS):
                # Update perim with the max value. DFS on water returns 1.
                # DFS on the unvisited island returns its actual total perimeter.
                perim = max(perim, dfs(r, c))

        return perim
