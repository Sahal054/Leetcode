"""
238. Product of Array Except Self (Optimal Two-Pass O(1) Space)

--- The Core Intuition ---
1. Two Independent Passes: Instead of trying to find the left and right products at the 
   exact same time, we do it in two separate steps using the `res` array to store our work.
2. Pass 1 (Left to Right): We iterate forward. For each element, we drop the current 
   `prefix` product into `res[i]`, and THEN multiply `prefix` by `nums[i]` for the next 
   element to use.
3. Pass 2 (Right to Left): We iterate backward. The `res` array already contains the 
   left products. We multiply whatever is already in `res[i]` by the current `postfix` 
   product, and THEN multiply `postfix` by `nums[i]` for the next element.

--- Visual Traversal Walkthrough ---

Example: nums = [1, 2, 3, 4]
Initial res  = [1, 1, 1, 1]

[ PASS 1: PREFIX (Left to Right) ]
- prefix = 1
- i=0: res[0] = 1.  prefix becomes 1 * 1 = 1
- i=1: res[1] = 1.  prefix becomes 1 * 2 = 2
- i=2: res[2] = 2.  prefix becomes 2 * 3 = 6
- i=3: res[3] = 6.  prefix becomes 6 * 4 = 24
* After Pass 1, res = [1, 1, 2, 6] (These are the left-side products)

[ PASS 2: POSTFIX (Right to Left) ]
- postfix = 1
- i=3: res[3] = 6 * 1 = 6.    postfix becomes 1 * 4 = 4
- i=2: res[2] = 2 * 4 = 8.    postfix becomes 4 * 3 = 12
- i=1: res[1] = 1 * 12 = 12.  postfix becomes 12 * 2 = 24
- i=0: res[0] = 1 * 24 = 24.  postfix becomes 24 * 1 = 24
* After Pass 2, res = [24, 12, 8, 6]

--- Complexity ---
- Time Complexity: $O(N)$. We loop through the array exactly twice. $N + N = 2N$, 
  which drops the constant to become $O(N)$.
- Space Complexity: $O(1)$ auxiliary space. The problem description explicitly states 
  that the output array `res` does not count toward space complexity. Since we only use 
  two integer variables (`prefix` and `postfix`), it takes $O(1)$ extra memory.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array with 1s
        res = [1] * len(nums)

        # PASS 1: Calculate all prefix products
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # PASS 2: Calculate all postfix products and multiply them with the prefixes
        postfix = 1
        # Loop backwards: start at len-1, stop at -1 (exclusive), step by -1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]
        
        return res
