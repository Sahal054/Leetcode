"""
994. Rotting Oranges (Multi-Source Breadth-First Search)

--- The Core Intuition ---
1. The Simultaneous Spread: Rotting doesn't happen one orange at a time; it happens 
   simultaneously from ALL currently rotten oranges. This means Depth-First Search (DFS) 
   is useless here. We need Breadth-First Search (BFS) to simulate the infection spreading 
   outward "level by level" (or minute by minute).
2. Multi-Source Queue: Instead of starting BFS from a single node, we scan the grid and 
   throw EVERY rotten orange into our queue at Minute 0. They will all act as ground zero.
3. The Fresh Counter: Instead of scanning the entire grid again at the end to see if we 
   missed any oranges, we count how many `fresh` oranges exist at the very beginning. 
   Every time we rot an orange, we do `fresh -= 1`. 
4. The Snapshot Loop: `for i in range(len(q)):` is the secret sauce for tracking time. 
   By grabbing the length of the queue *before* we start popping, we only process the 
   oranges that rotted in the *previous* minute. Newly rotted oranges are added to the 
   back of the queue and wait for the next minute to begin.

--- Visual Traversal Walkthrough ---

Example Grid:
[2, 1, 1]
[1, 1, 0]
[0, 1, 1]

[ INITIAL SETUP: MINUTE 0 ]
- Scan grid: found 1 rotten orange at (0,0). q = [(0,0)]
- Scan grid: found 6 fresh oranges. fresh = 6
- time = 0

[ MINUTE 1 ]
- snapshot size = 1. Pop (0,0).
- Check neighbors of (0,0):
  - Right (0,1) is fresh! Rot it. grid[0][1] = 2. fresh = 5. q = [(0,1)]
  - Down (1,0) is fresh! Rot it. grid[1][0] = 2. fresh = 4. q = [(0,1), (1,0)]
- Snapshot ends. time = 1.

[ MINUTE 2 ]
- snapshot size = 2. 
- Pop (0,1). Right is (0,2) -> Rot it! fresh = 3. q = [(1,0), (0,2)]
- Pop (1,0). Down is (2,0) -> Empty! Right is (1,1) -> Rot it! fresh = 2. q = [(0,2), (1,1)]
- Snapshot ends. time = 2.

[ FAST FORWARD ]
- Minute 3: (0,2) has no fresh neighbors. (1,1) rots (2,1). fresh = 1.
- Minute 4: (2,1) rots (2,2). fresh = 0.
- Loop breaks early because fresh is 0! 

[ RESOLUTION ]
- Return time (4). (If fresh was still > 0, we'd return -1 because an orange was trapped).

--- Complexity ---
- Time Complexity: $O(M \times N)$ where $M$ is rows and $N$ is columns. We visit each 
  cell in the grid at most once. (Note: Using `collections.deque` and `popleft()` is 
  crucial here, as a standard Python list `pop(0)` is $O(N)$ and degrades performance).
- Space Complexity: $O(M \times N)$ for the queue. In the worst-case scenario where the 
  entire grid is filled with rotten oranges at the start, the queue holds every single cell.
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Optimization: Use deque for O(1) pops from the left side of the queue
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0 

        # Step 1: Initialize the Multi-Source Queue and count fresh targets
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # Step 2: BFS level by level (minute by minute)
        # We only loop if there is a queue AND we still have fresh oranges left to infect
        while q and fresh > 0:

            # Take a snapshot of the queue length to only process this specific minute
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    rows = r + dr
                    cols = c + dc

                    # Check boundaries and ensure the neighbor is actually a fresh orange
                    if (rows not in range(ROWS) or 
                        cols not in range(COLS) or
                        grid[rows][cols] != 1):
                            continue   

                    # Infect it, add it to the queue for the next minute, and decrement count
                    grid[rows][cols] = 2
                    q.append((rows, cols))
                    fresh -= 1
                    
            # One full minute has passed
            time += 1
        
        # Step 3: Check if any isolated fresh oranges survived the apocalypse
        return time if fresh == 0 else -1
