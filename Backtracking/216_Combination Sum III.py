"""
216. Combination Sum III (Backtracking / Bounded Decision Tree)

--- The Core Intuition ---
1. Fixed, Naturally Sorted Pool (1 to 9): Unlike Combination Sum I and II where we are 
   handed an arbitrary unsorted array, our candidate pool here is always the distinct 
   integers `1` through `9`. Because they are already unique and sorted in ascending order, 
   we don't need `sort()` or a duplicate-skipping check (`nums[i] == nums[i - 1]`).
2. Dual Base-Case Constraints (`len == k` AND `total == n`): Hitting the target sum `n` is 
   no longer enough on its own—we must reach `n` using *exactly* `k` numbers. Likewise, 
   if we already have `k` numbers (`len(comb) >= k`) and haven't hit `n`, continuing is 
   pointless, so we prune immediately.
3. Single-Use + Forward-Only (`backtrack(i + 1, ...)`): Each number from `1` to `9` can be 
   used at most once, so we pass `i + 1` into the recursive call. Advancing `start` strictly 
   forward also prevents duplicate permutations (e.g., generating `[1, 2, 4]` once rather 
   than also generating `[2, 1, 4]`).
4. Early Loop Termination (`if total + i > n: break`): Because `i` increases from `start` 
   up to `9`, the moment `total + i > n`, every subsequent number in the loop will also 
   exceed `n`. Calling `break` stops the loop instantly without wasting recursive calls.

--- Decision Tree Graph (Visual Walkthrough) ---

Example: k = 3, n = 7
Format: [current_comb] (sum)

                                 [] (0)
          /             /           |           \
     pick 1          pick 2      pick 3      pick 4..9
       /               /            |            \
   [1] (1)          [2] (2)      [3] (3)      [4] (4) ...
    /    \           /    \         |            |
pick 2  pick 3   pick 3  pick 4  pick 4       pick 5
  /        \       /        \       |            |
[1,2](3) [1,3](4) [2,3](5) [2,4](6) [3,4](7)  4+5=9 > 7
 /   \      |       /        /     (len=2 < 3,  [BREAK!]
3     4   pick 4 pick 4   pick 5    next is 5:
|     |     |      |        |       7+5=12 > 7
v     v     v      v        v        [BREAK!])
[1,2,3](6) [1,2,4](7) [1,3,4](8) [2,3,4](9) [2,4,5](11)
 (len=3,   [HIT! k=3,  4+4=8>7    5+4=9>7    6+5=11>7
 total!=7)  total=7]   [BREAK!]   [BREAK!]   [BREAK!]
           Save [1,2,4]

(Note: At [1, 2] (3), after checking i=3 ([1, 2, 3] -> sum 6) and i=4 ([1, 2, 4] -> sum 7), 
when the loop reaches i=5, 3 + 5 = 8 > 7 triggers `break`, skipping 5, 6, 7, 8, and 9!)

--- Complexity ---
- Time Complexity: $O(k \times \binom{9}{k})$. Because the candidate pool is strictly fixed 
  to the 9 digits `{1..9}`, there are at most $\binom{9}{k}$ combinations of size `k` to 
  evaluate, and copying each valid combination into `res` takes $O(k)$ time.
- Space Complexity: $O(k)$ auxiliary space for the maximum depth of the recursive call stack 
  and the `comb` buffer list (excluding the memory required to store the output `res`).
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def backtrack(start, comb, total):
            # Base Case 1: Both constraints satisfied (exact sum 'n' AND exact count 'k')
            if total == n and len(comb) == k:
                res.append(comb.copy())
                return
            
            # Base Case 2 (Pruning): Overshot the target sum or exceeded 'k' elements
            if total > n or len(comb) >= k:
                return
            
            # Candidate pool is always integers 1 through 9
            for i in range(start, 10):
                # EARLY PRUNING: Since 'i' increases monotonically, all subsequent numbers
                # will also overshoot 'n'—break out of the loop immediately
                if total + i > n:
                    break
                
                # 1. MAKE A CHOICE
                comb.append(i)

                # 2. EXPLORE THAT CHOICE (pass 'i + 1' so each digit is used at most once)
                backtrack(i + 1, comb, total + i)

                # 3. UNDO THE CHOICE (Backtrack)
                comb.pop()
        
        # Start at digit 1 with an empty combination and a running total of 0
        backtrack(1, [], 0)
        return res
