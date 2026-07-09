"""
130. Surrounded Regions (Depth-First Search & Reverse Thinking)

The objective is to capture all regions on a 2D board that are completely surrounded 
by 'X'. A region is captured by flipping all its 'O's into 'X's. Crucially, any 'O' 
that touches the border of the board is NOT surrounded, and therefore any 'O' connected 
to a border 'O' is also safe from capture.

Instead of trying to find the surrounded regions directly (which is difficult because 
you don't know a region is surrounded until you check every single node in it), this 
solution uses "Reverse Thinking". It finds all the UNSURROUNDED regions first, marks 
them as safe, and then captures whatever is left over.

--- The Core Intuition ---
1. Phase 1: Border Scan & Mark Safe ('T'). 
   We iterate ONLY along the four borders of the grid. If we find an 'O', we know 
   it cannot be surrounded. We launch a DFS from that cell to find all connected 'O's 
   and temporarily mark them as 'T' (for Temporary or True/Safe).
2. Phase 2: Capture Surrounded Regions. 
   Now we scan the entire board. Any 'O' we see right now MUST be completely 
   surrounded, because if it wasn't, our Phase 1 DFS would have already reached it 
   and turned it into a 'T'. We flip these trapped 'O's to 'X'.
3. Phase 3: Restore Safe Regions. 
   We scan the board one last time. We find all our temporary 'T's (the safe regions) 
   and flip them back to their original 'O' state.

--- Visual Traversal Walkthrough ---

Example Grid:
  0 1 2 3
0 X X X X
1 X O O X
2 X X O X
3 X O X X

[ PHASE 1: Border Scan for 'O' ]
We check only rows 0 and 3, and columns 0 and 3.
- (0,0) to (0,3): All 'X'.
- (3,0): 'X'. 
- (3,1): Found 'O' on the bottom border!
  -> Run DFS(3, 1): Mark (3,1) as 'T'. 
  -> Check neighbors: up is 'X', down is out, left is 'X', right is 'X'. DFS ends.
- (3,2) to (3,3): All 'X'.
- Column borders: No new 'O's found.

Grid after Phase 1:
X X X X
X O O X  <- These 'O's were not touched because they don't connect to the border
X X O X
X T X X  <- This one was on the border, so it became 'T'

[ PHASE 2: Capture Remaining 'O's ]
We scan the whole grid. If we see an 'O', we change it to 'X'.
- We find 'O's at (1,1), (1,2), and (2,2). 
- We flip them to 'X'.

Grid after Phase 2:
X X X X
X X X X  <- Captured!
X X X X  <- Captured!
X T X X

[ PHASE 3: Restore 'T's back to 'O' ]
We scan the whole grid. If we see a 'T', we change it to 'O'.
- We find a 'T' at (3,1) and flip it back to 'O'.

Final Result:
X X X X
X X X X
X X X X
X O X X

--- Complexity ---
- Time Complexity: O(R * C) where R is rows and C is columns. Phase 1 visits cells 
  at most once during DFS. Phase 2 and 3 iterate through the grid exactly once.
- Space Complexity: O(R * C) in the worst case for the DFS recursion call stack 
  (e.g., if the entire board is filled with a snake-like pattern of 'O's).
"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            # Base cases: out of bounds, or the cell is not an 'O'
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            
            # Mark the cell as 'T' (Temporary/Safe)
            board[r][c] = "T"

            # Recursively visit all 4 neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # 1. (Phase 1) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                # Only launch DFS if we are on a border cell and it's an 'O'
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    dfs(r, c)
        
        # 2. (Phase 2) Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. (Phase 3) Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
