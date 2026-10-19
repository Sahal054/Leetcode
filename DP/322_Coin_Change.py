"""
322. Coin Change (Bottom-Up Tabulation Dynamic Programming)

The objective is to find the fewest number of coins needed to make up a given target 
'amount'. If that amount of money cannot be made up by any combination of the coins, 
return -1.

--- The Core Intuition: Building Up From Nothing ---
A greedy approach (always picking the largest coin first) fails here. For example, 
if coins = [1, 3, 4] and amount = 6, a greedy algorithm takes 4, then 1, then 1 (3 coins). 
But the optimal answer is 3 + 3 (2 coins). 

To solve this perfectly, we use Dynamic Programming (Tabulation). We build a 1D array 
'dp' where each index 'a' represents a sub-amount from $0 to the target amount. 
The value stored at dp[a] will be the absolute minimum number of coins needed to 
make that specific amount 'a'.

--- The State Transition Formula ---
To find the answer for a specific amount 'a', we look back at the answers we already 
calculated for smaller amounts:
$$dp[a] = \min(dp[a], 1 + dp[a - c])$$

Where:
- c: The value of the coin we are currently testing.
- dp[a - c]: The minimum coins needed to make the remaining balance after using coin 'c'.
- 1 + ...: Adding 1 to represent the physical coin 'c' we just used.

--- Visual DP Table Evolution ---

Example Input: coins = [1, 3, 4], amount = 6
Initial DP Table (size 7, filled with 'infinity' placeholder 7):
Indices (Amounts):   0    1    2    3    4    5    6
                  [ 0,   7,   7,   7,   7,   7,   7 ]
                    ^
                Base Case (0 amount takes 0 coins)

--- Step-by-Step Execution Trace ---

- amount = 1: Uses coin 1 -> 1 + dp[1-1] = 1 + dp[0] = 1. Table: [0, 1, 7, 7, 7, 7, 7]
- amount = 2: Uses coin 1 -> 1 + dp[2-1] = 1 + dp[1] = 2. Table: [0, 1, 2, 7, 7, 7, 7]
- amount = 3: 
    - Test coin 1 -> 1 + dp[3-1] = 1 + dp[2] = 3
    - Test coin 3 -> 1 + dp[3-3] = 1 + dp[0] = 1  (Min is 1). Table: [0, 1, 2, 1, 7, 7, 7]
- amount = 4: 
    - Test coin 4 -> 1 + dp[4-4] = 1 + dp[0] = 1  (Min is 1). Table: [0, 1, 2, 1, 1, 7, 7]
- amount = 5: 
    - Test coin 1 -> 1 + dp[5-1] = 1 + dp[4] = 2
    - Test coin 3 -> 1 + dp[5-3] = 1 + dp[2] = 3
    - Test coin 4 -> 1 + dp[5-4] = 1 + dp[1] = 2  (Min is 2). Table: [0, 1, 2, 1, 1, 2, 7]
- amount = 6: 
    - Test coin 3 -> 1 + dp[6-3] = 1 + dp[3] = 1 + 1 = 2 (Min is 2). Table: [0, 1, 2, 1, 1, 2, 2]

Final Value at dp[6] is 2!

--- Complexity ---
- Time Complexity: O(A * C) where A is the target amount and C is the number of coin types. 
  The nested loops run exactly (amount * len(coins)) times.
- Space Complexity: O(A) to allocate the 1D state tracking list up to size 'amount + 1'.
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the DP array. We use 'amount + 1' as a safe placeholder for infinity 
        # because the absolute maximum number of coins you could ever need is 'amount' (using $1 coins).
        dp = [amount + 1] * (amount + 1)
        
        # Base Case: It takes zero coins to make an amount of 0
        dp[0] = 0

        # Step up through every single sub-amount from 1 to the target amount
        for a in range(1, amount + 1):
            # Try applying every coin option to the current sub-amount
            for c in coins:
                # Security clearance: We can only use a coin if its value isn't bigger 
                # than the sub-amount we are trying to build
                if a - c >= 0:
                    # Update our table with the minimum coins option found
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        # If the value at our target index is still our 'infinity' placeholder, 
        # it means no combination of coins can make that amount. Return -1.
        return dp[amount] if dp[amount] != amount + 1 else -1


"""
322. Coin Change (Top-Down Dynamic Programming / Memoization)

--- The Core Intuition ---
1. The Overlapping Subproblem Cure: We know the brute force DFS recalculates the exact 
   same remainders over and over. To fix this, we introduce a `memo` dictionary (our cache). 
   Whenever we figure out the minimum coins needed for a specific remainder, we write 
   it down in our dictionary.
2. The Cache Intercept: At the very beginning of our `dfs` function, before we do any 
   looping or calculations, we ask: "Have we seen this remainder before?" If it's in 
   our `memo`, we instantly return the saved answer, completely short-circuiting that 
   entire branch of the recursion tree.
3. Time Travel: By caching results, we convert an exponentially growing tree into a 
   straightforward polynomial graph. We guarantee that we only ever calculate the answer 
   for each number from `1` to `amount` exactly ONE time.

--- Visual Traversal Walkthrough ---

Example: coins = [1, 2], amount = 3
Cache (memo) starts empty: {}

[ INITIAL CALL ]
- dfs(3): Not in memo. Try Coin 1 -> needs dfs(2).

[ BRANCHING WITH COIN 1 ]
- dfs(2): Not in memo. Try Coin 1 -> needs dfs(1).
  - dfs(1): Not in memo. Try Coin 1 -> needs dfs(0).
    - dfs(0): Base case, returns 0. (Cost: 1)
  - dfs(1) tries Coin 2 -> needs dfs(-1). Base case, returns inf.
  - dfs(1) finishes evaluating. Minimum is 1. 
  - CACHE IT: memo[1] = 1. Returns 1.
- dfs(2) tries Coin 2 -> needs dfs(0). Returns 0. (Cost: 1)
- dfs(2) finishes evaluating. Minimum is 1.
- CACHE IT: memo[2] = 1. Returns 1.
- Total for taking Coin 1 first: 1 + dfs(2) = 2.

[ BRANCHING WITH COIN 2 ]
- Try Coin 2 -> needs dfs(1).
- dfs(1): Wait! It IS in the memo! (memo[1] == 1). 
- INSTANT RETURN: returns 1 without doing any further recursion.
- Total for taking Coin 2 first: 1 + dfs(1) = 2.

[ RESOLUTION ]
- dfs(3) finishes. Minimum is 2.
- CACHE IT: memo[3] = 2. 
- Returns 2.

--- Complexity ---
- Time Complexity: $O(S \times N)$ where $S$ is the number of coin denominations and 
  $N$ is the target amount. Because of our cache, we only compute the answer for each 
  remainder (from $1$ to $N$) exactly once. During that single computation, we loop $S$ 
  times (once per coin). This is a massive optimization over the $O(S^N)$ brute force.
- Space Complexity: $O(N)$. We use $O(N)$ space for the recursive call stack (in the 
  worst case where we use all $1 coins) AND $O(N)$ space to store up to $N$ results 
  in our `memo` dictionary.
"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Our cache to store previously computed minimums for specific remainders
        memo = {}
        
        def dfs(rem):
            # Base Case 1: We made exact change!
            if rem == 0:
                return 0
            
            # Base Case 2: We overshot the amount.
            if rem < 0:
                return float('inf')
            
            # CACHE CHECK: If we already solved this remainder, return it instantly!
            if rem in memo:
                return memo[rem]
            
            min_coins = float('inf')
            
            # Branch out and try every single coin
            for coin in coins:
                res = dfs(rem - coin)
                
                if res != float('inf'):
                    min_coins = min(min_coins, 1 + res)
            
            # CACHE SAVE: Before returning, write down the answer for this remainder
            memo[rem] = min_coins
            return min_coins
            
        ans = dfs(amount)
        
        return ans if ans != float('inf') else -1
