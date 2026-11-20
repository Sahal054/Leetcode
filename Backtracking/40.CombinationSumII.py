"""
40. Combination Sum II — Optimized (Backtracking + Sorting + Pruning)

--- The Core Intuition ---
1. Why Sort First (`candidates.sort()`): Sorting unlocks two major upgrades. First, 
   it groups identical numbers together so we can skip duplicates. Second, it arranges 
   candidates from smallest to largest, allowing us to stop checking larger numbers the 
   instant our sum gets too big.
2. Early Loop Termination (`break` vs. `return`): In the unoptimized version, we had to 
   make a recursive call just to hit `if total > target: return` and bounce back. Because 
   the array is now sorted, if `total + candidates[i] > target`, we know every number 
   after `i` is even larger and will also overshoot. Using `break` instantly cuts off 
   the rest of the `for` loop without wasting a single recursive call!
3. Defensive Deduplication (`i > start and candidates[i] == candidates[i-1]`): While 
   standard LeetCode 39 guarantees distinct inputs, adding this check protects against 
   duplicate inputs (and is the exact rule used in Combination Sum II). `i > start` 
   ensures we only skip duplicate values *at the same tree level* (horizontal siblings), 
   while still allowing the first occurrence to reuse itself deeper in the recursion.
4. Unbounded Reuse (`backtrack(i, ...)`): Passing `i` instead of `i + 1` lets us keep 
   picking `candidates[i]` repeatedly until we either hit `target` or trigger `break`.

--- Decision Tree Graph (Visual Walkthrough) ---

Example: candidates = [2, 2, 3, 7], target = 7
(Using a duplicate '2' to show both the duplicate-skip AND the early 'break' pruning)

                                  [] (0)
          /                /                \              \
     i=0 (pick 2)     i=1 (skip 2)      i=2 (pick 3)    i=3 (pick 7)
         /               [SKIP]              /                \
     [2] (2)        (i > start &         [3] (3)            [7] (7)
    /    |   \       nums[1]==nums[0])   /      \           [HIT!]
i=0(2) i=1 i=2(3)                    i=2(3)   i=3(7)       Save [7]
  /    [X]    \                        /         \
[2,2](4)     [2,3](5)              [3,3](6)   3+7=10 > 7
 /   \        /     \               /     \     [BREAK!]
2     3    i=2(3)  i=3(7)       i=2(3)   i=3(7)
|     |      |       |            |
v     v      v       v            v
[2,2,2](6) [2,2,3](7) 5+3=8>7   6+3=9>7
 /         [HIT!]    [BREAK!]   [BREAK!]
2         Save [2,2,3]
|
v
6+2=8 > 7
[BREAK!] (Stops loop immediately; never even checks 3 or 7!)

--- Complexity ---
- Time Complexity: $O(N \log N + N^{\frac{T}{M} + 1})$ where $N$ is the number of 
  candidates, $T$ is `target`, and $M$ is the smallest candidate value. Sorting takes 
  $O(N \log N)$, and the backtracking tree explores at most $N^{\frac{T}{M} + 1}$ states 
  in the worst case—though `break` pruning dramatically shrinks the actual runtime.
- Space Complexity: $O(\frac{T}{M})$ auxiliary space for the maximum recursion stack 
  depth and the `comb` buffer list (excluding the output `res` list and Python's Timsort 
  auxiliary memory).
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Sort ascending to enable early 'break' pruning and duplicate skipping
        candidates.sort()
        res = []

        def backtrack(start, comb, total):
            # Base Case 1: Exact target reached; save a snapshot of the combination
            if total == target:
                res.append(comb.copy())
                return 
            
            # Base Case 2: Safety guard (rarely reached now thanks to pre-call 'break')
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicate values at the same decision level to avoid duplicate subsets
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # EARLY PRUNING: Since candidates is sorted, all subsequent numbers will also
                # exceed target—break out of the loop immediately without recursing
                if total + candidates[i] > target:
                    break
                
                # 1. MAKE A CHOICE
                comb.append(candidates[i])

                # 2. EXPLORE THAT CHOICE (pass 'i' to allow unlimited reuse of candidates[i])
                backtrack(i, comb, total + candidates[i])

                # 3. UNDO THE CHOICE (Backtrack)
                comb.pop()
                
        backtrack(0, [], 0)
        return res
