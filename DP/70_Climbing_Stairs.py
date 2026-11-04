"""
70. Climbing Stairs (Dynamic Programming - Fibonacci Style)

The problem asks for the number of distinct ways to reach the top of a 
staircase with 'n' steps, where you can move 1 or 2 steps at a time.


problem. To reach step 'n', you must have come from:
1. Step (n-1) — by taking a 1-step jump.
2. Step (n-2) — by taking a 2-step jump.

Therefore, the total ways to reach step 'n' is the sum of ways to reach 
the previous two steps. This follows the Fibonacci sequence.

Recurrence Relation:
$$f(n) = f(n-1) + f(n-2)$$


--- Visual Logic (Bottom-Up) ---

If n = 5, we can work backwards or forwards. Your code starts from the top 
and moves down (similar to the NeetCode diagram):

Stairs:  [0]  [1]  [2]  [3]  [4]  [5]
Ways:     8    5    3    2    1    1

Wait, why are there "1" ways at step 5? 
- At the very top (step 5), you are already there (1 way).
- At step 4, there is only 1 way to reach the top (one 1-step jump).

Step-by-step Trace for n = 5:

Initialization:
one = 1 (represents ways from current step)
two = 1 (represents ways from next step over)

Loop runs (n-1) = 4 times:

--- Iteration 1 ---
temp = 1
one = 1 + 1 = 2
two = 1
(Current state: 2 ways from step 3)

--- Iteration 2 ---
temp = 2
one = 2 + 1 = 3
two = 2
(Current state: 3 ways from step 2)

--- Iteration 3 ---
temp = 3
one = 3 + 2 = 5
two = 3
(Current state: 5 ways from step 1)

--- Iteration 4 ---
temp = 5
one = 5 + 3 = 8
two = 5
(Current state: 8 ways from step 0)

Final Result: 8
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: If n=1, there's only 1 way.
        # Your code handles this by not entering the loop if n=1.
        one = 1
        two = 1

        # We update 'one' to be the sum of the previous two values
        # effectively sliding our window across the Fibonacci sequence.
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one


"""

This solution uses an explicit DP array (memoization table) to store the 
number of ways to reach every step from 0 to n. It follows the same 
Fibonacci logic: the ways to reach step 'i' is the sum of ways to reach 
the two steps below it.

--- Visual Logic (The DP Table) ---

Example for n = 5:
Index (Step):  [0]  [1]  [2]  [3]  [4]  [5]
Ways:          [1]  [1]  [2]  [3]  [5]  [8]

1. Base Cases:
   - dp[0] = 1 (1 way to stay at the ground)
   - dp[1] = 1 (1 way to reach the 1st step: a single 1-step jump)

2. Filling the Table:
   - dp[2] = dp[1] + dp[0] = 1 + 1 = 2
   - dp[3] = dp[2] + dp[1] = 2 + 1 = 3
   - dp[4] = dp[3] + dp[2] = 3 + 2 = 5
   - dp[5] = dp[4] + dp[3] = 5 + 3 = 8

Final Result: dp[5] = 8
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Create an array of size n + 1
        dp = [0] * (n + 1)
        
        # Initialize base cases
        dp[0] = 1
        dp[1] = 1

        # Fill the table up to n
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]

"""
70. Climbing Stairs (Top-Down Dynamic Programming / Memoization)

--- The Core Intuition ---
1. The Decision Tree: At any given step `i`, you have exactly two choices: take a single 
   step (`i + 1`) or take a double step (`i + 2`). This creates a binary decision tree 
   branching all the way up to the top.
2. Counting Valid Paths: Because the problem asks for the "number of distinct ways" 
   (rather than the minimum steps), we accumulate the results of our branches using 
   addition (`+`). The total ways to reach the top from step `i` is the sum of the 
   ways from step `i + 1` and step `i + 2`.
3. The Overlapping Subproblem (The Fibonacci Link): Imagine climbing 5 stairs. You can 
   reach step 3 by taking (1+1+1) or (1+2) or (2+1). Regardless of *how* you got to 
   step 3, the number of ways to go from step 3 to step 5 is always the same. Without 
   a cache, plain recursion wildly recalculates these overlapping subproblems, running 
   in $O(2^N)$ time.
4. The Memoization: By caching the answer for a specific step `i` inside `memo`, we 
   ensure that the first time we calculate how to climb from step 3 to the top, we 
   never have to calculate it again. This elegantly collapses the exponential tree 
   into a linear path.

--- Visual Traversal Walkthrough ---

Example: n = 3
Cache starts empty: {}

[ INITIAL CALL ]
- dfs(0): Standing at the bottom.
- Branch 1 (Take 1 step): Needs dfs(1)
- Branch 2 (Take 2 steps): Needs dfs(2)

[ EXPLORING BRANCH 1 ]
- dfs(1): Standing on step 1.
  - Take 1 step: Needs dfs(2)
  - Take 2 steps: Needs dfs(3) -> Base Case 1! Reached the top. Returns 1.
  
  [ EXPLORING dfs(2) FROM INSIDE dfs(1) ]
  - dfs(2): Standing on step 2.
    - Take 1 step: dfs(3) -> Returns 1.
    - Take 2 steps: dfs(4) -> Base Case 2! Overstepped. Returns 0.
    - Total for dfs(2): 1 + 0 = 1. 
    - CACHE IT: memo[2] = 1. Returns 1.
    
  - Back to dfs(1): Total is dfs(2) + dfs(3) -> 1 + 1 = 2.
  - CACHE IT: memo[1] = 2. Returns 2.

[ EXPLORING BRANCH 2 ]
- dfs(2): Wait! It IS in the memo! (memo[2] == 1).
- INSTANT RETURN: returns 1 without doing any further recursion.

[ RESOLUTION ]
- Back to dfs(0): Total is dfs(1) + dfs(2) -> 2 + 1 = 3.
- CACHE IT: memo[0] = 3. 
- Returns 3.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the total number of stairs. Because of our `memo` 
  dictionary, we calculate the answer for each step from 0 to $N$ exactly ONE time.
- Space Complexity: $O(N)$ to store the `memo` dictionary and for the depth of the 
  recursive call stack (which will drill straight down $N$ times before returning).
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(i):
            # Base Case 1: Reached the exact top step (1 valid way)
            if i == n:
                return 1
            
            # Base Case 2: Overstepped the top (0 valid ways)
            if i > n:
                return 0
                
            # CACHE CHECK: If we've already calculated paths from this step, return it!
            if i in memo:
                return memo[i]
            
            # Recursively calculate taking 1 step and taking 2 steps
            # Total ways = (Ways if we step 1) + (Ways if we step 2)
            memo[i] = dfs(i + 1) + dfs(i + 2)
            
            # CACHE SAVE
            return memo[i]
            
        # Start climbing from step 0
        return dfs(0)
        
