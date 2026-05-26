"""
213. House Robber II (Dynamic Programming - Circular Neighborhood)

The constraint that makes this problem distinct from House Robber I is that the 
houses are arranged in a CIRCLE. This means the first house and the last house 
are direct neighbors. If you rob the first house, you cannot rob the last house.

--- The Circular House Trick ---
To solve a circular problem, we break the circle into two linear sub-problems:
1. Sub-problem A: Skip the first house. Rob from House[1] to House[n-1].
2. Sub-problem B: Skip the last house.  Rob from House[0] to House[n-2].

By taking the maximum result of these two linear scenarios (and the single first 
house itself for the edge case of an array with 1 item), we solve the circle!

Recurrence Relation for each linear scan:
$$f(n) = \max(\text{nums}[n] + f(n-2), f(n-1))$$



--- Visual Dynamic Programming Representation ---

Example Input: nums = [1, 2, 3, 1]

       [ 1 ] --- [ 2 ]
         |         |      <- The houses form a loop!
       [ 1 ] --- [ 3 ]

Scenario 1: Skip the First House -> nums[1:] = [2, 3, 1]
   Linear Scan Trace:
   - Initial: rob1 = 0, rob2 = 0
   - House 2: temp = max(2 + 0, 0) = 2 -> rob1 = 0, rob2 = 2
   - House 3: temp = max(3 + 0, 2) = 3 -> rob1 = 2, rob2 = 3
   - House 1: temp = max(1 + 2, 3) = 3 -> rob1 = 3, rob2 = 3
   Result A = 3

Scenario 2: Skip the Last House -> nums[:-1] = [1, 2, 3]
   Linear Scan Trace:
   - Initial: rob1 = 0, rob2 = 0
   - House 1: temp = max(1 + 0, 0) = 1 -> rob1 = 0, rob2 = 1
   - House 2: temp = max(2 + 0, 1) = 2 -> rob1 = 1, rob2 = 2
   - House 3: temp = max(3 + 1, 2) = 4 -> rob1 = 2, rob2 = 4
   Result B = 4

Final calculation: max(nums[0], Result A, Result B) -> max(1, 3, 4) -> 4

--- Complexity ---
- Time Complexity: O(n) because we run our linear helper function twice, 
  visiting the houses a maximum of 2 times.
- Space Complexity: O(1) as we only use temporary variables (rob1, rob2, temp) 
  to track values rather than creating full allocation arrays.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # max(nums[0]) protects against single element arrays like nums = [2]
        # where the slices would return empty lists [0]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        # Standard House Robber I linear space-optimized algorithm
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
