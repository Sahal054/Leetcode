"""
39. Combination Sum (Backtracking / Unbounded Decision Tree)

--- The Core Intuition ---
1. Unlimited Reuse (Passing 'i' instead of 'i + 1'): In standard Combinations (LeetCode 77), 
   we passed `i + 1` so we wouldn't reuse the same element. Here, the problem allows us to 
   pick the same number as many times as we want. Passing `i` into the recursive call lets 
   us stay on `candidates[i]` until we hit or exceed the target.
2. Preventing Duplicate Permutations (The 'start' Pointer): Why don't we start the `for` 
   loop at `0` every time? Because `[2, 2, 3]` and `[2, 3, 2]` are the same combination! 
   By restricting choices to `range(start, len(candidates))`, once we move past `2` to `3`, 
   we are never allowed to look backward and pick `2` again.
3. Pruning Dead Ends (`total > target`): Because all candidates are positive integers, 
   once `total` exceeds `target`, adding more numbers will never bring it back down. 
   Returning immediately prunes entire subtrees of wasted work.
4. The Backtrack & Deep Copy: We mutate a single `comb` list in place (`append` -> 
   recurse -> `pop`) for $O(1)$ state transitions, and save `comb.copy()` whenever 
   `total == target` so subsequent `pop()` calls don't erase our saved answers.

--- Decision Tree Graph (Visual Walkthrough) ---

Example: candidates = [2, 3, 6, 7], target = 7
Format: [current_comb] (sum)

                              [] (0)
          /             /               \            \
     pick 2          pick 3           pick 6        pick 7
       /               /                 \              \
   [2] (2)          [3] (3)           [6] (6)        [7] (7) -> [HIT! Save [7]]
    /    \           /    \            /    \
pick 2  pick 3   pick 3  pick 6    pick 6  pick 7
  /        \       /        \        /        \
[2,2](4) [2,3](5) [3,3](6) [3,6](9) [6,6](12) [6,7](13)
 /   \      |       /        [X]      [X]       [X]
2     3     3    pick 3    (Pruned) (Pruned)  (Pruned)
|     |     |      |
v     v     v      v
[2,2,2](6) [2,2,3](7) [2,3,3](8) [3,3,3](9)
 /   \      |          [X]        [X]
2     3   [HIT!]     (Pruned)   (Pruned)
|     |   Save [2,2,3]
v     v
[2,2,2,2](8) [2,2,2,3](9)
  [X]          [X]
(Pruned)     (Pruned)

(Note: Notice how [3] (3) NEVER branches left to pick 2, and [6] (6) NEVER branches 
left to pick 2 or 3. That one-way forward rule guarantees zero duplicate combinations!)

--- Complexity ---
- Time Complexity: $O(N^{\frac{T}{M} + 1})$ where $N$ is the number of candidates, $T$ is 
  the target value, and $M$ is the smallest candidate value. In the worst case, the decision 
  tree branches up to $N$ ways at each step and reaches a maximum depth of $T / M$ (e.g., 
  repeatedly picking the smallest number until reaching `target`).
- Space Complexity: $O(\frac{T}{M})$ auxiliary space for the maximum depth of the recursive 
  call stack and the `comb` buffer list (excluding the memory required to store the output `res`).
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, comb, total):
            # Base Case 1: Exact match found! Save a snapshot of the current combination
            if total == target:
                res.append(comb.copy())
                return 
            
            # Base Case 2 (Pruning): Overshot the target; stop exploring this branch
            if total > target:
                return
            
            # Explore all candidates starting from 'start' to avoid duplicate permutations
            for i in range(start, len(candidates)):
                # 1. MAKE A CHOICE
                comb.append(candidates[i])

                # 2. EXPLORE THAT CHOICE
                # Pass 'i' (not i + 1) because we are allowed to reuse candidates[i]
                backtrack(i, comb, total + candidates[i])

                # 3. UNDO THE CHOICE (Backtrack)
                comb.pop()
                
        # Start at index 0 with an empty combination and a running total of 0
        backtrack(0, [], 0)
        return res
