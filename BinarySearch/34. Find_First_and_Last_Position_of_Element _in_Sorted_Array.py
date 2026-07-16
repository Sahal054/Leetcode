"""
34. Find First and Last Position of Element in Sorted Array (Binary Search)

The objective is to find the starting and ending position of a given target value 
in an array of integers sorted in non-decreasing order. If the target is not found, 
return [-1, -1]. The algorithm must run in O(log n) time complexity.

Instead of finding the target and then linearly scanning left and right (which would 
degrade to O(n) time in the worst case), this solution uses Binary Search twice: 
once to find the absolute leftmost occurrence, and once to find the absolute rightmost.

--- The Core Intuition ---
1. Standard Binary Search Limitation: A normal binary search stops as soon as it finds 
   *any* instance of the target. If there are duplicates, it might land in the middle 
   of them.
2. The "Bias" Concept: We modify the binary search to take a `leftbias` boolean flag.
3. Left Bias (Finding the First Position): When we find the target, we record its 
   index (`i = m`), but we DO NOT stop. We pretend there might be another target 
   even further to the left, so we aggressively move our right boundary (`r = m - 1`).
4. Right Bias (Finding the Last Position): When we find the target, we record its 
   index, but we pretend there might be another target further to the right. We 
   aggressively move our left boundary (`l = m + 1`).

--- Visual Traversal Walkthrough ---

Example Array: nums = [5, 7, 7, 8, 8, 10], target = 8

[ PASS 1: Search with Left Bias (leftbias = True) ]
Initial state: l = 0, r = 5, i = -1

- Iteration 1:
  m = 2. nums[2] is 7.
  8 > 7, so target is to the right. l = 3.

- Iteration 2:
  l = 3, r = 5. m = 4. nums[4] is 8.
  Match! We found an 8. 
  Record i = 4. 
  Because leftbias is True, we keep searching LEFT to see if there's an earlier one.
  r = m - 1 = 3.

- Iteration 3:
  l = 3, r = 3. m = 3. nums[3] is 8.
  Match! We found another 8.
  Record i = 3 (overwriting 4).
  leftbias is True, keep searching LEFT.
  r = m - 1 = 2.

- Loop terminates (l <= r is now 3 <= 2, which is False).
Result of Pass 1: Leftmost index is 3.

[ PASS 2: Search with Right Bias (leftbias = False) ]
Initial state: l = 0, r = 5, i = -1

- Iteration 1:
  m = 2. nums[2] is 7.
  8 > 7, move right. l = 3.

- Iteration 2:
  l = 3, r = 5. m = 4. nums[4] is 8.
  Match! We found an 8.
  Record i = 4.
  Because leftbias is False, we keep searching RIGHT to see if there's a later one.
  l = m + 1 = 5.

- Iteration 3:
  l = 5, r = 5. m = 5. nums[5] is 10.
  8 < 10, target is to the left.
  r = m - 1 = 4.

- Loop terminates (l <= r is now 5 <= 4, which is False).
Result of Pass 2: Rightmost index is 4.

Final Return: [3, 4]

--- Complexity ---
- Time Complexity: O(log n) because we are running two standard binary searches. 
  O(log n) + O(log n) = O(log n).
- Space Complexity: O(1) as we are only using a few variables for pointers (l, r, m, i) 
  and no additional data structures.
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binsearch(nums, target, leftbias):
            l, r = 0, len(nums) - 1
            # i stores the most recent index where we found the target
            i = -1
            
            while l <= r:
                m = l + (r - l) // 2

                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    # Target found! Record the index.
                    i = m

                    # If leftbias is True, aggressive search to the left
                    if leftbias:
                        r = m - 1
                    # If leftbias is False, aggressive search to the right
                    else:
                        l = m + 1
            return i
        
        # Run binary search twice to find both boundaries
        left = binsearch(nums, target, True)
        right = binsearch(nums, target, False)

        return [left, right]
