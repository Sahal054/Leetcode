"""
518. Coin Change II (Top-Down Dynamic Programming / Memoization)

--- The Core Intuition ---
1. The 2D State Space: Because we need to avoid counting duplicate combinations 
   (like [1, 2] and [2, 1] as separate answers), we must lock our recursion to a 
   specific coin index. Our state requires two variables: `i` (which coin we are 
   currently considering) and `rem` (the remaining amount).
2. The Binary Choice: At any given coin `i`, we have exactly two choices:
   - SKIP: We decide we are completely done with `coins[i]`. We move to `i + 1` 
     and keep the same remainder.
   - TAKE: We decide to use `coins[i]`. We subtract its value from the remainder. 
     Crucially, because we have an INFINITE supply, we do NOT move to `i + 1`. 
     We stay at index `i` so we can potentially take the exact same coin again!
3. The Accumulation: Unlike Coin Change 1 (where we wanted the `min()` of the branches), 
   we want the total number of ways. So, we simply add the results of our two branches 
   together: `Total Ways = Skip + Take`.
4. The Memoization: We cache the result of `(i, rem)` so that if we arrive at the same 
   coin with the same remaining amount via a different path, we instantly return the 
   saved number of combinations.

--- Visual Traversal Walkthrough ---

Example: coins = [1, 2], amount = 3

[ INITIAL CALL ]
- dfs(i=0, rem=3): Standing at Coin 1 (value: 1).
  - Choice 1 (Skip): dfs(1, 3) -> Move to Coin 2.
  - Choice 2 (Take): dfs(0, 2) -> Stay at Coin 1, amount becomes 2.

[ EXPLORING 'TAKE' BRANCH (Staying on Coin 1) ]
- dfs(0, 2): 
  - Skip: dfs(1, 2)
  - Take: dfs(0, 1)
    - dfs(0, 1):
      - Skip: dfs(1, 1)
      - Take: dfs(0, 0) --> BASE CASE! rem == 0. Returns 1. (We found path: [1,1,1])

[ EXPLORING 'SKIP' BRANCHES (Moving to Coin 2) ]
- dfs(1, 3): Standing at Coin 2 (value: 2).
  - Skip: dfs(2, 3) --> BASE CASE! Out of bounds. Returns 0.
  - Take: dfs(1, 1)
    - dfs(1, 1): 
      - Skip: dfs(2, 1) -> Returns 0.
      - Take: dfs(1, -1) -> BASE CASE! Overshot (rem < 0). Returns 0.
      - Total for dfs(1, 1) = 0 + 0 = 0.
  - Total for dfs(1, 3) = 0 + 0 = 0.

[ CACHE HITS IN ACTION ]
- As the tree unfolds, paths like `dfs(1, 1)` or `dfs(1, 2)` will be evaluated. 
- When another branch attempts to calculate `dfs(1, 1)`, it hits the `memo` dictionary 
  and instantly returns the sum without traversing down to the base cases again.

--- Complexity ---
- Time Complexity: $O(C \times N)$ where $C$ is the number of coins and $N$ is the 
  target amount. There are $C \times N$ unique combinations of `(index, remainder)`, 
  and our memoization dictionary ensures we only ever calculate each combination exactly once.
- Space Complexity: $O(C \times N)$ to store the states in the `memo` dictionary, plus 
  $O(N)$ for the recursive call stack (if we repeatedly take a coin of value 1).
"""

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        memo = {}

        def dfs(i, rem):
            # Base Case 1: We successfully hit exact change! 
            # This path counts as 1 valid combination.
            if rem == 0:
                return 1
            
            # Base Case 2: We overshot the amount OR we ran out of coins to check.
            # This path is a dead end, contributing 0 valid combinations.
            if rem < 0 or i == len(coins):
                return 0
            
            # CACHE CHECK
            if (i, rem) in memo:
                return memo[(i, rem)]
            
            # Choice 1: SKIP the current coin entirely.
            # Move to the next coin (i + 1), remainder stays the same.
            skip = dfs(i + 1, rem)
            
            # Choice 2: TAKE the current coin.
            # Stay on the current coin (i) so it can be reused, subtract its value.
            take = dfs(i, rem - coins[i])
            
            # The total ways to make change from this state is the sum of both choices
            memo[(i, rem)] = skip + take
            return memo[(i, rem)]
            
        return dfs(0, amount)
