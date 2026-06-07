"""
840. Magic Squares In Grid (Sliding 3x3 Window Matrix Scan)

The objective is to find how many 3x3 contiguous subgrids within a larger grid 
form a "Magic Square". A magic square is a 3x3 grid filled with distinct digits 
from 1 to 9 where every row, column, and diagonal sums to the exact same number (15).

--- The Core Intuition: Sliding Sub-Grid Validation ---
Since a magic square must strictly be 3x3, we can bound our outer search loops 
so they stop 2 rows and 2 columns before the true edges of the grid. This sets 
up a sliding 3x3 viewport. 

For every top-left coordinate (r, c) we discover, we run 4 security clearings:
1. Unique Range Verification: Ensure all 9 numbers are distinct and between 1 and 9.
2. Row Sum Verification: Each of the 3 horizontal lines must equal 15.
3. Column Sum Verification: Each of the 3 vertical lines must equal 15.
4. Diagonal Sum Verification: Both cross diagonals must equal 15.

--- Why 15? ---
The sum of numbers from 1 to 9 is 45 ($1 + 2 + \dots + 9 = 45$). Since there are 
3 rows sharing these numbers evenly, each individual row must sum up to $45 / 3 = 15$.

--- Visual 3x3 Matrix Coordinates Layout ---

      c          c+1        c+2
  +----------+----------+----------+
r |  [r][c]  | [r][c+1] | [r][c+2] |  ---> Row Sum Check
  +----------+----------+----------+
r+1| [r+1][c] |[r+1][c+1]|[r+1][c+2]|
  +----------+----------+----------+
r+2| [r+2][c] |[r+2][c+1]|[r+2][c+2]|
  +----------+----------+----------+
       |          |          |
       V          V          V
             Column Sum Checks



--- Step-by-Step Execution Trace ---

Example Subgrid located at (r=0, c=0):
    4   9   2
    3   5   7
    8   1   6

1. Unique Check:
   - Evaluates all cells. Values collected: {1, 2, 3, 4, 5, 6, 7, 8, 9}. 
   - All distinct, all within [1, 9]. Check passes.

2. Row Sums Check:
   - Row 0: 4 + 9 + 2 = 15 (Pass)
   - Row 1: 3 + 5 + 7 = 15 (Pass)
   - Row 2: 8 + 1 + 6 = 15 (Pass)

3. Column Sums Check:
   - Col 0: 4 + 3 + 8 = 15 (Pass)
   - Col 1: 9 + 5 + 1 = 15 (Pass)
   - Col 2: 2 + 7 + 6 = 15 (Pass)

4. Diagonal Sums Check:
   - Main Diagonal (Top-Left to Bottom-Right): 4 + 5 + 6 = 15 (Pass)
   - Anti-Diagonal (Top-Right to Bottom-Left): 2 + 5 + 8 = 15 (Pass)

All conditions met! The helper function returns 1, incrementing our total count.

--- Complexity ---
- Time Complexity: O(R * C) where R is rows and C is columns. Although we run 
  multiple internal loops inside 'magic()', they run a fixed constant number 
  of times (exactly 3x3 grid size ops), simplifying down to constant O(1) space matrix checks.
- Space Complexity: O(1) auxiliary space because the 'values' set stores a maximum 
  of 9 elements at any given execution instant.
"""

from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def magic(r, c):
            values = set()

            # Phase 1: Range & Unique Check
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    # Check if number is duplicated or outside the 1-9 threshold
                    if val in values or not (1 <= val <= 9):
                        return 0
                    values.add(val)

            # Phase 2: Horizontal Row Sums
            for i in range(r, r + 3):
                if sum(grid[i][c:c+3]) != 15:
                    return 0

            # Phase 3: Vertical Column Sums
            for i in range(c, c + 3):
                if (grid[r][i] + grid[r + 1][i] + grid[r + 2][i]) != 15:
                    return 0

            # Phase 4: Diagonal Cross Sums
            if (
                grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or  # Main diagonal
                grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15    # Anti-diagonal
            ): 
                return 0
                
            return 1         

        res = 0
        # Iterate and slide the 3x3 viewport across the valid window frames
        for r in range(ROW - 2):
            for c in range(COL - 2):
                res += magic(r, c)
                
        return res
