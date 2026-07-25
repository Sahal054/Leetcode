"""
45. Jump Game II (Greedy / Implicit BFS)

The objective is to find the *minimum* number of jumps required to reach the last index. 
You are guaranteed that you can always reach the last index.

While this is technically a 1D array problem, the most optimal way to think about this 
solution is as an implicit Breadth-First Search (BFS) using a sliding window. 

--- The Core Intuition ---
1. Window of Opportunity: We use two pointers, `l` (left) and `r` (right), to define a 
   "window" of indices we can currently reach. 
2. Implicit BFS Levels: 
   - Level 0 (0 jumps): We start at index 0. Our window is `[0, 0]`.
   - Level 1 (1 jump): The furthest we can reach from Level 0.
   - Level 2 (2 jumps): The furthest we can reach from any node in Level 1.
3. Finding the Farthest Jump: For our current window `[l, r]`, we iterate through every 
   index inside it. We calculate the farthest possible reach (`i + nums[i]`) across all 
   these indices. 
4. Shifting the Window: Once we check the whole current window, we have finished one "jump". 
   We increment our jump counter (`res`). Our new window starts right after our old window 
   (`l = r + 1`), and ends at the `farthest` point we just discovered (`r = farthest`).
5. The Exit: We stop the loop as soon as our right pointer `r` reaches or exceeds the last 
   index of the array.

--- Visual Traversal Walkthrough ---

Example: nums = [2, 3, 1, 1, 4]

[ INITIAL SETUP ]
- res = 0 (jumps)
- l = 0, r = 0 (Current window: index 0 to 0)
- Target is index 4 (len(nums) - 1).

[ JUMP 1 ]
- r (0) < 4. We enter the loop.
- Loop through current window [0, 0]:
  - i = 0 (value = 2): farthest = max(0, 0 + 2) = 2.
- Window check complete. 
- We took 1 jump (res = 1).
- Shift window: l becomes r + 1 (1). r becomes farthest (2).
- New Window: indices [1, 2]

[ JUMP 2 ]
- r (2) < 4. We enter the loop.
- Loop through current window [1, 2]:
  - i = 1 (value = 3): farthest = max(2, 1 + 3) = 4.
  - i = 2 (value = 1): farthest = max(4, 2 + 1) = 4.
- Window check complete.
- We took 1 jump (res = 2).
- Shift window: l becomes r + 1 (3). r becomes farthest (4).
- New Window: indices [3, 4]

[ END ]
- r (4) is no longer < 4. Loop terminates.
- Return res (2).

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the length of `nums`. Even though there is a nested 
  `for` loop inside a `while` loop, the pointers `l` and `r` only move forward. Every index 
  in the array is visited exactly once.
- Space Complexity: $O(1)$. We are only storing a few integer pointers (`l`, `r`, `farthest`, 
  `res`), so it requires no additional scaling memory.
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0      # Counts the minimum number of jumps
        l = 0        # Left boundary of our current jump window
        r = 0        # Right boundary of our current jump window

        # Keep jumping until our right boundary reaches or passes the last index
        while r < len(nums) - 1:
            farthest = 0
            
            # Iterate through all indices in the current window
            for i in range(l, r + 1):
                # Calculate the maximum reach from the current index
                farthest = max(farthest, i + nums[i])
            
            # Move the window to the next "level" of jumps
            l = r + 1          # Next window starts right after the current one
            r = farthest       # Next window ends at the farthest point we can reach
            res += 1           # Increment jump count because we transitioned windows
            
        return res
