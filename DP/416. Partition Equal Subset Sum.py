"""
416. Partition Equal Subset Sum (Top-Down Dynamic Programming / 0/1 Knapsack)

--- The Core Intuition ---
1. The Mathematical Reduction: Splitting an array into two subsets with equal sums means 
   each subset MUST equal `total // 2`. First, if `total` is odd, an equal split is 
   impossible, so we immediately return `False`. Second, we don't actually need to find 
   *two* subsets—if we find *one* subset that sums to `target = total // 2`, the leftover 
   numbers are mathematically guaranteed to sum to `target` as well.
2. 0/1 Knapsack vs. Unbounded Knapsack: Unlike Coin Change (where we could reuse the same 
   coin infinitely by staying at index `i`), here each number in `nums` can only be used 
   AT MOST ONCE. Therefore, whether we include or exclude `nums[i]`, both recursive calls 
   must advance to `i + 1`.
3. Boolean Accumulation (`or`): We aren't counting *how many* ways we can hit the target; 
   we only care if *at least one* valid combination exists. Using `include or exclude` 
   allows a single `True` from any valid branch to bubble all the way up to the root.
4. Overlapping Subproblems: Different combinations of earlier numbers can add up to the 
   exact same sum. For example, in `[1, 2, 3, 6]`, picking `{1, 2}` or picking `{3}` both 
   bring you to index 3 with `target_left = 3`. Caching `(i, target_left)` prevents 
   re-evaluating the remainder of the array from identical states.

--- Visual Traversal Walkthrough ---

Example: nums = [1, 2, 3]
Total sum = 6 (even) -> target = 3.
Cache starts empty: memo = {}

[ INITIAL CALL ]
- dfs(i=0, target_left=3): Standing at nums[0] = 1.
  - Choice 1 (Include 1): dfs(1, 3 - 1) -> dfs(1, 2)
  - Choice 2 (Exclude 1): dfs(1, 3)

[ EXPLORING 'INCLUDE' BRANCH: dfs(1, 2) ]
- Standing at nums[1] = 2, need 2 more.
  - Include 2: dfs(2, 2 - 2) -> dfs(2, 0)
    -> BASE CASE 1! target_left == 0. Found subset [1, 2]! Returns True.
  - Exclude 2: dfs(2, 2) (Standing at nums[2] = 3, need 2 more)
    - Include 3: dfs(3, 2 - 3) -> dfs(3, -1) -> BASE CASE 2! Overshot (< 0). Returns False.
    - Exclude 3: dfs(3, 2) -> BASE CASE 2! Out of bounds (i >= 3). Returns False.
    - CACHE: memo[(2, 2)] = False.
  - Resolution for dfs(1, 2): True or False -> True.
  - CACHE: memo[(1, 2)] = True.

[ EXPLORING 'EXCLUDE' BRANCH: dfs(1, 3) ]
- Standing at nums[1] = 2, need 3 more.
  - Include 2: dfs(2, 1) -> tries 3 (overshoots) and skips 3 (out of bounds) -> False.
  - Exclude 2: dfs(2, 3) (Standing at nums[2] = 3, need 3 more)
    - Include 3: dfs(3, 3 - 3) -> dfs(3, 0) -> BASE CASE 1! Found subset [3]! Returns True.
  - CACHE: memo[(1, 3)] = True.

[ RESOLUTION ]
- Back at dfs(0, 3): True or True -> True.
- CACHE: memo[(0, 3)] = True. Returns True.

--- Complexity ---
- Time Complexity: $O(N \times T)$ where $N$ is the number of elements in `nums` and $T$ 
  is `sum(nums) // 2` (the target sum). There are at most $N \times T$ unique `(i, target_left)` 
  states, and our `memo` dictionary ensures each state is computed at most once in $O(1)$ time.
- Space Complexity: $O(N \times T)$ to store all possible states in the `memo` cache, 
  plus $O(N)$ for the maximum depth of the recursive call stack.
"""

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        
        # If the total sum is odd, it is mathematically impossible to split it into two equal integers
        if total % 2 != 0:
            return False
            
        # Reduce the problem to finding a single subset that equals half the total
        target = total // 2
        memo = {}
        
        def dfs(i, target_left):
            # Base Case 1: We perfectly hit the target sum!
            if target_left == 0:
                return True
                
            # Base Case 2: We overshot the target (negative) or ran out of numbers to pick
            if target_left < 0 or i >= len(nums):
                return False
                
            # CACHE CHECK: Return the saved boolean if we've already evaluated this state
            if (i, target_left) in memo:
                return memo[(i, target_left)]
                
            # Choice 1: INCLUDE the current number (subtract its value and advance to i + 1)
            include = dfs(i + 1, target_left - nums[i])
            
            # Choice 2: EXCLUDE the current number (keep target as is and advance to i + 1)
            exclude = dfs(i + 1, target_left)
            
            # If either path reaches 0, this state can form a valid partition
            memo[(i, target_left)] = include or exclude
            
            return memo[(i, target_left)]
            
        # Start at index 0 with the full target remaining
        return dfs(0, target)
