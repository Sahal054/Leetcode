"""
77. Combinations (Backtracking / Decision Tree)

--- The Core Intuition ---
1. Dynamic Nested Loops: If `k = 2`, you could solve this with two nested `for` loops. 
   But what if `k = 10`? You can't dynamically write 10 nested loops. Backtracking is 
   essentially a way to recursively generate an arbitrary number of nested loops!
2. Preventing Duplicates (The 'Start' Variable): A combination means `[1, 2]` is the 
   exact same as `[2, 1]`. To prevent calculating both, we enforce a strict left-to-right 
   rule. If we pick `2`, the next recursive call must only pick from numbers `3` and 
   beyond (`i + 1`). This forces our decision tree to only grow forward.
3. The Backtrack (The Undo Step): We use a single shared list `comb` to build our paths 
   to save memory. But because it's shared, when we hit a dead end or finish a valid 
   combination, we MUST remove (`pop()`) the last element we added. This cleans up the 
   workspace so the next branch can use it.
4. The Deep Copy Trap: When `len(comb) == k`, we have a valid combination. We MUST append 
   `comb.copy()` (or `comb[:]`) to our result array. If we just wrote `res.append(comb)`, 
   we would be appending a *reference* to the exact same list that we are constantly 
   popping from. By the end of the algorithm, our result would just be a list of empty arrays!

--- Visual Traversal Walkthrough ---

Example: n = 4, k = 2
Initial state: res = [], comb = []

[ STARTING AT 1 ]
- backtrack(start=1, comb=[])
- Loop i from 1 to 4:
  - i = 1: 
    - comb.append(1)  ->  comb = [1]
    - Call backtrack(2, [1])

[ EXPLORING FROM 1 ]
- backtrack(start=2, comb=[1])
- Loop i from 2 to 4:
  - i = 2: 
    - comb = [1, 2] -> BASE CASE HIT (len == 2)! 
    - res = [[1, 2]] (Appended a COPY).
    - comb.pop() -> comb = [1]
  - i = 3:
    - comb = [1, 3] -> BASE CASE HIT! 
    - res = [[1, 2], [1, 3]]
    - comb.pop() -> comb = [1]
  - i = 4:
    - comb = [1, 4] -> BASE CASE HIT! 
    - res = [[1, 2], [1, 3], [1, 4]]
    - comb.pop() -> comb = [1]
- Backtrack finishes for i = 1. 

[ THE UNDO ]
- Back in the top level loop (i = 1):
  - comb.pop() -> comb = [] (Clean workspace for the next number!)

[ STARTING AT 2 ]
- Loop moves to i = 2:
  - comb.append(2) -> comb = [2]
  - Call backtrack(3, [2])
  - explores [2, 3], [2, 4], pops back to []...

[ RESOLUTION ]
- Tree fully traversed. 
- Return res: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

--- Complexity ---
- Time Complexity: $O(k \times \binom{n}{k})$. The mathematical formula for "n choose k" is 
  $\binom{n}{k}$, which dictates exactly how many valid combinations exist. For every single 
  valid combination, we do $O(k)$ work to create a `.copy()` of the array to store in `res`.
- Space Complexity: $O(k)$ auxiliary space. The recursive call stack goes exactly `k` levels 
  deep. The `comb` list also takes up exactly $O(k)$ space. (We do not count the memory used 
  by the `res` output array in standard auxiliary space analysis).
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(start, comb):
            # Base Case: We have gathered exactly 'k' elements
            if len(comb) == k:
                # CRITICAL: Append a COPY of the list. 
                # Otherwise, future pop() operations will erase this valid combination!
                res.append(comb.copy())
                return # Optimization: We can return here to skip unnecessary looping
            
            # Explore all valid numbers from the current 'start' up to 'n'
            for i in range(start, n + 1):
                
                # 1. MAKE A CHOICE
                comb.append(i)
                
                # 2. EXPLORE THAT CHOICE
                # We pass 'i + 1' to ensure we only pick numbers strictly larger than 'i'
                backtrack(i + 1, comb)
                
                # 3. UNDO THE CHOICE (Backtrack)
                # Remove 'i' so the loop can safely try the next number in the same position
                comb.pop()
        
        # Start exploring with number 1 and an empty combination list
        backtrack(1, [])
        
        return res
