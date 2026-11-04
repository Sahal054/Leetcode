"""
46. Permutations (Backtracking / Decision Tree)

--- The Core Intuition ---
1. Permutations vs. Combinations: In combinations, `[1, 2]` and `[2, 1]` are identical, 
   so we used a `start` variable to strictly look forward and prevent reverse duplicates. 
   In permutations, order matters! `[2, 1]` is a brand new valid answer. Therefore, 
   we drop the `start` variable entirely. At every step, we loop through the ENTIRE 
   input array from index 0.
2. The Cycle-Check (Avoiding Duplicates): If we loop through the whole array every time, 
   how do we prevent picking `[1, 1, 1]`? We introduce a filter: `if nums[i] in comb`. 
   This checks our current path. If we are holding a `1`, we skip it and move to the 
   next number. This guarantees we use each number exactly once per permutation.
3. The Backtrack (The Undo Step): Exactly like combinations, we share a single `comb` 
   array in memory. We make a choice (`append`), explore that choice (`backtracking`), 
   and then undo the choice (`pop`) to clean the slate for the next iteration.
4. The Deep Copy Trap: When `len(comb) == len(nums)`, we have built a complete permutation. 
   We must append `comb.copy()` to `res`. If we appended the reference to `comb`, the 
   subsequent `pop()` operations would destroy our saved answers.

--- Visual Traversal Walkthrough ---

Example: nums = [1, 2, 3]
Initial state: res = [], comb = []

[ LEVEL 0: EMPTY PATH ]
- Loop i from 0 to 2:
  - i=0 (num=1): Not in comb. Append 1 -> comb=[1]. Recurse.

[ LEVEL 1: PATH IS [1] ]
- Loop i from 0 to 2:
  - i=0 (num=1): 1 IS in comb. Skip!
  - i=1 (num=2): Not in comb. Append 2 -> comb=[1, 2]. Recurse.

[ LEVEL 2: PATH IS [1, 2] ]
- Loop i from 0 to 2:
  - i=0 (num=1): Skip!
  - i=1 (num=2): Skip!
  - i=2 (num=3): Not in comb. Append 3 -> comb=[1, 2, 3]. Recurse.

[ LEVEL 3: BASE CASE ]
- comb is [1, 2, 3]. Length is 3 (len(nums)). 
- res.append(copy) -> res = [[1, 2, 3]]
- Return back to Level 2.

[ BACKTRACKING IN ACTION ]
- Back in Level 2: comb.pop() -> comb=[1, 2]
- Level 2 loop finishes. 
- Back in Level 1: comb.pop() -> comb=[1]
- Level 1 loop moves to i=2 (num=3):
  - Append 3 -> comb=[1, 3]. Recurse.
  - Inside [1, 3], i=0 (skip), i=1 (num=2). Append 2 -> comb=[1, 3, 2]. Base case!
  - res = [[1, 2, 3], [1, 3, 2]]
  - Pop 2. Pop 3.
- Level 1 loop finishes.
- Back in Level 0: comb.pop() -> comb=[]
- Level 0 loop moves to i=1 (num=2)... 

[ RESOLUTION ]
- Tree fully traversed. 
- Returns 6 permutations (3 factorial).

--- Complexity ---
- Time Complexity: $O(N \times N!)$ where $N$ is the length of `nums`. There are mathematically 
  $N!$ (N factorial) possible permutations. For each permutation, we take $O(N)$ time to 
  perform `.copy()`. Note: The `if nums[i] in comb` check also takes $O(N)$ time since it 
  searches a list. (For a massive array, we would use a `visited` boolean array or a set 
  to make that check $O(1)$, but for LeetCode constraints of N <= 6, searching the list is perfectly fine).
- Space Complexity: $O(N)$ auxiliary space for the recursive call stack depth and the 
  `comb` list itself.
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtracking(comb):
            # Base Case: The combination has used every number in the input array
            if len(comb) == len(nums):
                # CRITICAL: Append a COPY of the list to prevent reference wiping
                res.append(comb.copy())
                return
            
            # Loop through the ENTIRE input array every single time (no 'start' index)
            for i in range(len(nums)):
                
                # CYCLE-CHECK: If the number is already in our path, skip it
                if nums[i] in comb:
                    continue 
                
                # 1. MAKE A CHOICE
                comb.append(nums[i])
                
                # 2. EXPLORE THAT CHOICE
                backtracking(comb)
                
                # 3. UNDO THE CHOICE (Backtrack)
                comb.pop()
                
        # Start exploring with an empty path
        backtracking([]) 
        
        # Don't forget to return the final result!
        return res

class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]

        perm = self.permute(nums[1:])
        res =[]
        for p in perm:
            for i in range(len(p) +1):
                p_copy =p[:]
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res 

#this is constructive recursion
# - Time complexity: O(n^2 * n!)
# - Space complexity: O(n * n!)

class Solution(object):
    def permute(self, nums):
        n = len(nums)
        ans ,sol = [],[]

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans                    

#Recursive backtracking
