"""
300. Longest Increasing Subsequence (1D Dynamic Programming)

The goal is to find the length of the longest strictly increasing subsequence 
from an array of integers. This solution utilizes a bottom-up, backward 1D 
Dynamic Programming approach, evaluating the array from right to left.

--- The Core Intuition & Recurrence Relation ---
We initialize a 'dp' array of the same length as 'nums', filled entirely with 1s. 
This is because any single number on its own forms a valid increasing subsequence 
of length 1.

For each element at index i, we look ahead at every element at index j (where j > i). 
If nums[i] < nums[j], it means nums[i] can cleanly prepend onto the increasing 
subsequence already established starting at index j.

Formula from the screenshot:
$$dp[i] = \max(dp[i], 1 + dp[j]) \quad \text{for all } j > i \text{ if } \text{nums}[i] < \text{nums}[j]$$


--- Visual DP Grid Layout (nums = [1, 2, 4, 3]) ---

Following the NeetCode screenshot example, we build the solution from the end:

   Indices:       [0]      [1]      [2]      [3]
   nums =       [  1  ]  [  2  ]  [  4  ]  [  3  ]
              +--------+--------+--------+--------+
   Initial dp = |   1  |   1  |   1  |   1  |
              +--------+--------+--------+--------+
   Final dp =   |   3  |   2  |   1  |   1  |
              +--------+--------+--------+--------+
                                              ^
                                              Max value inside dp is 3

--- Step-by-Step Trace ---

--- Iteration 1 (i = 3): nums[3] = 3 ---
- Inner loop range(4, 4) is empty because there are no elements to its right.
- dp[3] remains 1.
- State: dp = [1, 1, 1, 1]

--- Iteration 2 (i = 2): nums[2] = 4 ---
- j = 3 (nums[3] = 3):
    - Check if nums[2] < nums[3] -> 4 < 3? False. (Crossed out with red X in screenshot)
- dp[2] remains 1.
- State: dp = [1, 1, 1, 1]

--- Iteration 3 (i = 1): nums[1] = 2 ---
- j = 2 (nums[2] = 4):
    - Check 2 < 4? True -> dp[1] = max(1, 1 + dp[2]) = max(1, 1 + 1) = 2
- j = 3 (nums[3] = 3):
    - Check 2 < 3? True -> dp[1] = max(2, 1 + dp[3]) = max(2, 1 + 1) = 2
- State: dp = [1, 2, 1, 1]

--- Iteration 4 (i = 0): nums[0] = 1 ---
- j = 1 (nums[1] = 2):
    - Check 1 < 2? True -> dp[0] = max(1, 1 + dp[1]) = max(1, 1 + 2) = 3
- j = 2 (nums[2] = 4):
    - Check 1 < 4? True -> dp[0] = max(3, 1 + dp[2]) = max(3, 1 + 1) = 3
- j = 3 (nums[3] = 3):
    - Check 1 < 3? True -> dp[0] = max(3, 1 + dp[3]) = max(3, 1 + 1) = 3
- State: dp = [3, 2, 1, 1]

Final Answer: max(dp) -> max([3, 2, 1, 1]) -> 3

--- Complexity ---
- Time Complexity: O(n^2) due to the nested loops checking all subsequent elements.
- Space Complexity: O(n) to store the 1D dp array.
"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Every single element is an increasing subsequence of length 1
        dp = [1] * len(nums)

        # Iterate backwards through the array
        for i in range(len(nums) - 1, -1, -1):
            # Check all elements to the right of the current element i
            for j in range(i + 1, len(nums)):
                # If the current element is smaller, it can extend the subsequence at j
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        # The answer is the maximum value found anywhere in our DP table
        return max(dp)
