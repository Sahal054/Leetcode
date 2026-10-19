"""
198. House Robber (Dynamic Programming - Space Optimized)

The objective is to find the maximum amount of money you can rob from a row of 
houses, with the constraint that you cannot rob two adjacent houses. 


For any house, you have two choices:
1. Rob this house: You get its value + the max you could rob starting 2 houses away.
2. Skip this house: You get the max you could rob starting from the next house.

Formula from the screenshot:
rob = max(arr[0] + rob[2:n], rob[1:n])



--- Visual Logic ---

Example Input: [1, 2, 3, 1]

   [ 1 ]      [ 2 ]      [ 3 ]      [ 1 ]
  House 0    House 1    House 2    House 3

We use two variables to track our progress:
rob1: Max loot up to house (i - 2)
rob2: Max loot up to house (i - 1)

Step-by-step Trace:

Initialization:
rob1 = 0
rob2 = 0

--- Iteration 1 (n = 1) ---
temp = max(1 + 0, 0) = 1
Update: rob1 = 0, rob2 = 1
(Current best loot: 1)

--- Iteration 2 (n = 2) ---
temp = max(2 + 0, 1) = 2
Update: rob1 = 1, rob2 = 2
(Current best loot: 2 - decided to rob House 1 instead of House 0)

--- Iteration 3 (n = 3) ---
temp = max(3 + 1, 2) = 4
Update: rob1 = 2, rob2 = 4
(Current best loot: 4 - decided to rob House 0 and House 2: 1 + 3)

--- Iteration 4 (n = 1) ---
temp = max(1 + 2, 4) = 4
Update: rob1 = 4, rob2 = 4
(Final result is 4)


--- Why this is Efficient ---
- Time Complexity: O(n) as we visit each house exactly once.
- Space Complexity: O(1) because we only store two variables (rob1, rob2) 
  instead of an entire array of size n.
"""



class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 represents max loot ending 2 houses ago [n-2]
        # rob2 represents max loot ending 1 house ago [n-1]
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            # At current house n, decide: 
            # Rob current + rob1 OR skip current and keep rob2
            temp = max(n + rob1, rob2)
            
            # Slide the window forward
            rob1 = rob2
            rob2 = temp
            
        return rob2
