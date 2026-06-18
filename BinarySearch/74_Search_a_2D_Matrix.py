"""
74. Search a 2D Matrix (Double Binary Search Strategy)

The objective is to determine if a target integer exists within an M x N matrix. 
The matrix has two special properties that make it a perfect candidate for binary search:
1. Each row is sorted in ascending order from left to right.
2. The first integer of each row is strictly greater than the last integer of the previous row.

--- The Core Intuition: Two-Stage Filtering ---
Because the rows are stacked in a continuous sorted sequence, we can think of this 
as a giant sorted 1D array broken up into rows. Instead of scanning line-by-line (O(M*N)), 
your solution uses a highly efficient "Double Binary Search" approach:

Phase 1 (Find the Row): Binary search vertically down the rows. We inspect the boundary 
values (first and last elements) of a middle row to deduce whether our target lives 
above it, below it, or directly inside its boundaries.

Phase 2 (Find the Column): Once the correct row is locked down, run a standard horizontal 
binary search within that single row to locate the target.

--- Visual 2D Matrix Search Layout ---

Example Input: matrix = [ [1,   3,  5,  7], 
                          [10, 11, 16, 20], 
                          [23, 30, 34, 60] ], target = 3

       cols:      0      1      2      3
  top (row 0) -> [ 1,    3,     5,    7 ]  <--- Target (3) falls within this row's boundaries!
  row (row 1) -> [10,   11,    16,   20 ]
  bot (row 2) -> [23,   30,    34,   60 ]

--- Step-by-Step Execution Trace ---

Initialization:
ROWS = 3, COLS = 4
top = 0, bottom = 2

--- Phase 1: Row Search ---
Iteration 1:
- Calculate middle row: row = 0 + (2 - 0) // 2 = 1
- Inspect Row 1 boundaries: First element is 10, Last element is 20.
- Check condition: Is target (3) > 20? No.
- Check condition: Is target (3) < 10? Yes!
- Decision: Target must be in a row higher up. Shift bottom marker: bottom = row - 1 = 0

Iteration 2:
- Calculate middle row: row = 0 + (0 - 0) // 2 = 0
- Inspect Row 0 boundaries: First element is 1, Last element is 7.
- Check condition: Is 3 > 7? No.
- Check condition: Is 3 < 1? No.
- Decision: Target safely falls within [1, 7]. Execute 'break' to lock row 0.

--- Phase 2: Column Search within Row 0 ---
Pointers: l = 0, r = 3, row = 0

Iteration 1:
- Calculate midpoint column: m = 0 + (3 - 0) // 2 = 1
- Evaluate matrix[0][1] = 3
- Compare with target: Does 3 == 3? YES!
- Match located! Returns True.

--- Complexity ---
- Time Complexity: O(log M + log N), where M is the number of rows and N is the 
  number of columns. The first binary search takes log M steps, and the second 
  takes log N steps. This is incredibly faster than searching cell-by-cell.
- Space Complexity: O(1) because the tracking boundaries are adjusted completely 
  in-place using basic pointer variables.
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS, COLS = len(matrix), len(matrix[0])

        # --- PHASE 1: Find the target row ---
        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            row = top + (bottom - top) // 2

            # If target is larger than the largest item in this row, look down
            if target > matrix[row][-1]:
                top = row + 1
            # If target is smaller than the smallest item in this row, look up
            elif target < matrix[row][0]:
                bottom = row - 1
            # Otherwise, target falls within this row's starting and ending range
            else:
                break
        
        # If the pointers cross without a break, the target is out of total matrix bounds
        if not (top <= bottom):
            return False
        
        # --- PHASE 2: Find the column inside the confirmed row ---
        l, r = 0, COLS - 1
        row = top + (bottom - top) // 2  # Re-identifies our locked-down row target
        
        while l <= r:
            m = l + (r - l) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
                
        return False
