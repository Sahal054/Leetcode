"""
55. Jump Game (Greedy / Backwards)

--- The Core Intuition ---
1. Shift the Goalpost: Instead of figuring out how to get from the start to the end, 
   we start at the end. We set our `target` to the very last index.
2. Work Backwards: We iterate backward through the array, starting from the second-to-last 
   item, moving towards index 0.
3. The Greedy Check: At each step, we look at our current index `i` and its maximum jump 
   `nums[i]`. If `i + nums[i]` is greater than or equal to our `target`, it means we 
   can reach the target from index `i`.
4. Update the Target: Because we know we can reach the old target from `i`, index `i` 
   becomes our NEW target! If you can reach `i`, you can definitely reach the end.
5. The Exit: After iterating through the whole array, if our `target` has been successfully 
   shifted all the way back to index 0, it means a valid path exists from start to finish.

--- Visual Traversal Walkthrough ---

Example: nums = [2, 3, 1, 1, 4]

[ INITIAL SETUP ]
- target = 4 (the last index)
- Loop starts at index 3 and goes backwards to 0.

[ i = 3, value = 1 ]
- Can we reach target(4) from index 3?
- 3 + nums[3] -> 3 + 1 = 4.
- 4 >= 4 (target). Yes!
- New target = 3.

[ i = 2, value = 1 ]
- Can we reach target(3) from index 2?
- 2 + nums[2] -> 2 + 1 = 3.
- 3 >= 3 (target). Yes!
- New target = 2.

[ i = 1, value = 3 ]
- Can we reach target(2) from index 1?
- 1 + nums[1] -> 1 + 3 = 4.
- 4 >= 2 (target). Yes! (We can overshoot it, which is perfectly fine).
- New target = 1.

[ i = 0, value = 2 ]
- Can we reach target(1) from index 0?
- 0 + nums[0] -> 0 + 2 = 2.
- 2 >= 1 (target). Yes!
- New target = 0.

[ END ]
- Loop finishes. target == 0. Return True.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the length of `nums`. We do exactly one pass 
  through the array from right to left.
- Space Complexity: $O(1)$. We are only updating a single integer variable (`target`), 
  requiring zero extra memory allocations. This makes it far superior to the DFS approach.
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Start our target at the very last index
        target = len(nums) - 1

        # Iterate backwards from the second-to-last element down to index 0
        for i in range(len(nums) - 1, -1, -1):
            
            # If the current index + its jump strength can reach or pass the target
            if i + nums[i] >= target:
                # Shift the goalpost: this index is our new target
                target = i
        
        # If we successfully shifted the target all the way to the start, we win
        return True if target == 0 else False



"""
55. Jump Game (DFS with Memoization)

--- The Core Intuition ---
1. The Setup: We use a recursive function `dfs(target)` where `target` represents 
   our current index in the array. 
2. The Base Cases: 
   - If our current index is greater than or equal to the last index, we made it! Return True.
   - If the value at our current index is 0, we are stuck. Return False.
   - If we have already visited this index and it didn't lead to the end, return False.
3. Exploring Jumps: We look at the maximum jump we can take `nums[target]`. We use a 
   loop to try the largest jump first (`nums[target]` down to 1). 
4. Memoization (The Secret Sauce): If a jump branch fails, we add our current index 
   to the `visit` set. This guarantees that if another path brings us to this same 
   index later, we instantly know it's a dead end without recalculating everything.

--- Visual Traversal Walkthrough ---

Example: nums = [2, 3, 1, 1, 4]

[ INITIAL SETUP ]
- target = 0 (value is 2). 

[ DFS(0) ]
- We can jump 1 or 2 steps. We try the biggest jump first (2).
- Call DFS(0 + 2) -> DFS(2)

[ DFS(2) ]
- target = 2 (value is 1).
- We can jump 1 step.
- Call DFS(2 + 1) -> DFS(3)

[ DFS(3) ]
- target = 3 (value is 1).
- We can jump 1 step.
- Call DFS(3 + 1) -> DFS(4)

[ DFS(4) ]
- target = 4. This is the last index! Return True.
- True bubbles all the way back up to DFS(0). We win.

(Note: If the array was [3, 2, 1, 0, 4], we would eventually hit index 3, get stuck, 
return False, add index 3 to `visit`, and backtrack to try smaller jumps).

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the length of `nums`. Because of the `visit` 
  set (memoization), we evaluate each index in the array at most one single time.
- Space Complexity: $O(N)$ for the recursion stack (if we take 1 step at a time) 
  and the `visit` set which can store up to $N$ indices.
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visit = set()

        def dfs(target):
            # Base case: we reached or passed the last index
            if target >= len(nums) - 1:
                return True
            
            # Base case: we landed on a zero and are stuck
            if nums[target] == 0:
                return False
            
            # Base case: we already know this index is a dead end
            if target in visit:
                return False
            
            # Try jumping. Start with the largest jump and decrement down to 1.
            for i in range(nums[target], 0, -1):
                # If any jump leads to the end, bubble up True
                if dfs(target + i):
                    return True
                
                # If a jump failed, mark the current target as a dead end
                visit.add(target)
                
            return False
        
        return dfs(0)
