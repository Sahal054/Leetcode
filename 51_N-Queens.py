"""
51. N-Queens (Backtracking with Mathematical Diagonal Hashing)

The goal is to place N non-attacking queens on an N×N chessboard. Since a queen can 
attack in any row, column, or diagonal line, every choice we make blocks multiple 
future paths. 

--- The Core Intuition: Row-by-Row Strategy ---
Instead of searching blindly across the entire board, we place exactly one queen per 
row, moving from top to bottom (r = 0 to n-1). This guarantees we never have horizontal 
conflicts, cutting down our search space massively.

To block columns and diagonals instantly without scanning lines, we use three tracking sets:
1. col: Tracks columns that already contain a queen.
2. posDig (Positive Diagonals): Tracks lines running from bottom-left to top-right.
3. negDig (Negative Diagonals): Tracks lines running from top-left to bottom-right.

--- The Brilliant Diagonal Math Trick ---
Every square on a specific diagonal shares a mathematical constant based on its coordinates:
- On a Positive Diagonal ( / ), the row and column indices always add up to the same number:
  r + c = Constant
- On a Negative Diagonal ( \ ), the row minus the column index always equals the same number:
  r - c = Constant



--- Visual Diagonal Constant Maps (4x4 Board) ---

   Positive Diagonals (r + c)              Negative Diagonals (r - c)
     c=0   c=1   c=2   c=3                   c=0   c=1   c=2   c=3
  +-----+-----+-----+-----+               +-----+-----+-----+-----+
r=0|  0  |  1  |  2  |  3  |             r=0|  0  | -1  | -2  | -3  |
  +-----+-----+-----+-----+               +-----+-----+-----+-----+
r=1|  1  |  2  |  3  |  4  |             r=1|  1  |  0  | -1  | -2  |
  +-----+-----+-----+-----+               +-----+-----+-----+-----+
r=2|  2  |  3  |  4  |  5  |             r=2|  2  |  1  |  0  | -1  |
  +-----+-----+-----+-----+               +-----+-----+-----+-----+
r=3|  3  |  4  |  5  |  6  |             r=3|  3  |  2  |  1  |  0  |
  +-----+-----+-----+-----+               +-----+-----+-----+-----+

--- Step-by-Step Execution Trace (N=4, First Path) ---

1. Row 0: Place Queen at c=0 frame -> board[0][0] = 'Q'
   - Block: col={0}, posDig={0}, negDig={0}

2. Row 1: 
   - c=0? Blocked by col (0)
   - c=1? Blocked by posDig/negDig (1+1=2, 1-1=0)
   - c=2? Free! -> Place Queen at board[1][2] = 'Q'
   - Block: col={0, 2}, posDig={0, 3}, negDig={0, -1}

3. Row 2:
   - c=0? Blocked by col (0)
   - c=1? Blocked by posDig (2+1=3)
   - c=2? Blocked by col (2)
   - c=3? Blocked by negDig (2-3=-1)
   - DEAD END! No columns work in Row 2.

4. Backtrack! 
   - Row 1 un-chooses c=2. Tracking sets wipe those values out.
   - Row 1 moves to c=3... and the exploration continues!



--- Complexity ---
- Time Complexity: O(N!). We have N options for the first queen, roughly N-2 for the next, etc. 
  The hashing sets keep the verification time at O(1) per square.
- Space Complexity: O(N^2) to maintain the state of the string board layout grid, plus O(N) 
  for the tracking sets and recursion stack.
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDig = set()  # Stores (r + c)
        negDig = set()  # Stores (r - c)

        res = []
        # Create an empty NxN board filled with dots
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # Base Case: All rows are filled safely (from 0 to n-1)
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Scan through every column choice in the current row
            for c in range(n):
                # Guard Condition: Skip columns or diagonals currently under attack
                if c in col or (r - c) in negDig or (r + c) in posDig:
                    continue

                # 1. Choose: Commit the queen position and hash the danger zones
                col.add(c)
                posDig.add(r + c)
                negDig.add(r - c)
                board[r][c] = "Q"

                # 2. Explore: Advance down to the next row
                backtrack(r + 1)

                # 3. Un-choose (Backtrack): Erase the footprint to test the next column option
                col.remove(c)
                posDig.remove(r + c)
                negDig.remove(r - c)
                board[r][c] = "."

        # Start the recursive search engine from row 0
        backtrack(0)
        return res
