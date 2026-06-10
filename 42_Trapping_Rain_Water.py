"""
42. Trapping Rain Water (Two-Pointer Greedy Strategy)

The objective is to compute how much water a terrain grid can trap after raining. 
The elevation map is represented by an array of non-negative integers where the 
width of each bar is 1.

--- The Core Intuition: Shifting the Bottleneck ---
The amount of water that can be trapped above any single bar at index 'i' is entirely 
determined by its bounding walls. Specifically, it depends on the maximum height 
to its left and the maximum height to its right. 

Formula for a single bar:
$$\text{Water trapped at index } i = \min(\text{leftMax}, \text{rightMax}) - \text{height}[i]$$

Instead of pre-computing arrays of max heights from both sides (which takes O(n) space), 
this solution uses two moving pointers (`l` and `r`) to solve it in-place with O(1) space.

--- The Key Trick ---
We compare `leftMax` and `rightMax`. Whichever wall is smaller acts as the true 
bottleneck. If `leftMax < rightMax`, we can confidently process the left pointer because 
no matter what tall bars exist in the middle, the water height over the left bar is 
guaranteed to be limited by `leftMax`.



--- Visual Elevation Layout ---

Example Input: height = [3, 1, 2, 4]

      4 |                 ██
      3 |   ██            ██
      2 |   ██      ██    ██
      1 |   ██  ██  ██    ██
  Floor +---+---+---+---+---+
  Index:    0   1   2   3

--- Step-by-Step Execution Trace ---

Initialization:
l = 0, r = 3
leftMax = height[0] = 3
rightMax = height[3] = 4
res = 0

--- Iteration 1 ---
- Condition check: Is l < r? (0 < 3 is True)
- Compare Max boundaries: Is leftMax < rightMax? (3 < 4 is True)
    - Action: Advance left pointer -> l = 1 (height[1] = 1)
    - Update leftMax: max(3, 1) = 3
    - Add trapped water: res += (leftMax - height[1]) -> res += (3 - 1) = 2
    - Current State: res = 2

--- Iteration 2 ---
- Condition check: Is l < r? (1 < 3 is True)
- Compare Max boundaries: Is leftMax < rightMax? (3 < 4 is True)
    - Action: Advance left pointer -> l = 2 (height[2] = 2)
    - Update leftMax: max(3, 2) = 3
    - Add trapped water: res += (leftMax - height[2]) -> res += (3 - 2) = 1
    - Current State: res = 2 + 1 = 3

--- Iteration 3 ---
- Condition check: Is l < r? (2 < 3 is True)
- Compare Max boundaries: Is leftMax < rightMax? (3 < 4 is True)
    - Action: Advance left pointer -> l = 3 (height[3] = 4)
    - Update leftMax: max(3, 4) = 4
    - Add trapped water: res += (leftMax - height[3]) -> res += (4 - 4) = 0
    - Current State: res = 3

The while loop terminates because l is no longer less than r (3 < 3 is False).
Final Result: 3

--- Complexity ---
- Time Complexity: O(n) because we move the left or right pointer inward by one 
  position per step, reading each element exactly once.
- Space Complexity: O(1) auxiliary space since we maintain everything using pointers 
  and value variables rather than dynamically sizing new data arrays.
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
            
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            # If the left wall is lower, it dictates the bottleneck for the left side
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])  # Update the ceiling height
                res += leftMax - height[l]         # Add trapped water layer
            # If the right wall is lower or equal, it dictates the bottleneck for the right side
            else:
                r -= 1
                rightMax = max(rightMax, height[r]) # Update the ceiling height
                res += rightMax - height[r]         # Add trapped water layer
                
        return res
