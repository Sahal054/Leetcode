"""
704. Binary Search (Divide and Conquer Pointer Strategy)

The objective is to find a target value within a sorted integer array. If the target 
exists, return its index; otherwise, return -1.

--- The Core Intuition: Halving the Search Space ---
Because the input array is already strictly SORTED, we do not need to check every single 
element one by one (which would take O(n) time). Instead, we look at the exact middle 
element:
1. If the middle value IS our target, we are done!
2. If the middle value is LARGER than the target, then the target must live in the 
   left half. We completely throw away the right half by moving our right pointer.
3. If the middle value is SMALLER than the target, then the target must live in the 
   right half. We completely throw away the left half by moving our left pointer.

By eliminating half of the remaining elements at every step, the search space collapses 
incredibly fast.

--- Visual Search Strategy Layout ---

Example Input: nums = [-1, 0, 3, 5, 9, 12], target = 9

Indices:    0      1      2      3      4      5
         +------+------+------+------+------+------+
         |  -1  |  0   |  3   |  5   |  9   |  12  |
         +------+------+------+------+------+------+
            ^              ^                    ^
            |              |                    |
         l (Left)       m (Mid)              r (Right)

--- Step-by-Step Execution Trace ---

Initialization:
l = 0
r = 5

--- Iteration 1 ---
- Check condition: Is l <= r? (0 <= 5 is True)
- Calculate Midpoint: m = (0 + 5) // 2 = 2
- Evaluate middle value: nums[2] = 3
- Compare with target: Is 3 == 9? No.
- Decide next step: Since 3 < 9 (nums[m] < target), the target must be on the right side.
- Shift Left boundary: l = m + 1 = 3

--- Iteration 2 ---
- Check condition: Is l <= r? (3 <= 5 is True)
- Calculate Midpoint: m = (3 + 5) // 2 = 4
- Evaluate middle value: nums[4] = 9
- Compare with target: Is 9 == 9? YES!
- Match found! The code immediately returns the index: 4

--- Complexity ---
- Time Complexity: O(log n). With every loop iteration, the number of elements we 
  have to search is cut strictly in half.
- Space Complexity: O(1) auxiliary space because we only maintain three pointer 
  variables (l, r, m) to look at elements in place.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # Note on Midpoint calculation:
            # m = (r + l) // 2 works perfectly in Python.
            # In other languages (like Java/C++), if r and l are very large, 
            # adding them could cause an integer overflow error. To prevent that, 
            # the safer alternative calculation is: m = l + (r - l) // 2
            m = (r + l) // 2
            
            # If the middle element is too big, target is in the left half
            if nums[m] > target:
                r = m - 1
            # If the middle element is too small, target is in the right half
            elif nums[m] < target:
                l = m + 1
            # Target located exactly at index m
            else:
                return m
                
        # If l and r pointers cross each other, the target is not in the array
        return -1
