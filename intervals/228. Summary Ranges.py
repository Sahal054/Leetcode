"""
228. Summary Ranges (Two Pointers / Array Scan)

--- The Core Intuition ---
1. The Anchor and Explorer: This is a classic string/array parsing pattern. We use an 
   anchor (`start`) to mark the beginning of a potential sequence, and an explorer (`i`) 
   to look ahead and see how far the sequence goes.
2. The Continuity Check: We know numbers are in a contiguous range if the next number 
   is exactly 1 greater than the current number (`nums[i]+1 == nums[i+1]`). The inner 
   `while` loop continuously consumes these consecutive numbers.
3. The Breakpoint: When the inner loop finishes, the chain has broken. We look at where 
   our explorer (`nums[i]`) ended up compared to our anchor (`start`). 
   - If they are different, we traversed a multi-number range, so we format it with an arrow.
   - If they are the same, the sequence broke immediately, meaning it's a standalone number.
4. Linear Traversal: Even though there is a `while` loop inside a `while` loop, the 
   index `i` never resets or goes backward. It strictly moves forward, making this highly 
   efficient.

--- Visual Traversal Walkthrough ---

Example: nums = [0, 1, 2, 4, 5, 7]

[ INITIAL SETUP ]
- i = 0
- res = []

[ FINDING FIRST RANGE ]
- i = 0: start = 0
- Inner loop checks: 
  - nums[0]+1 == nums[1] (0+1 == 1)? YES. i = 1
  - nums[1]+1 == nums[2] (1+1 == 2)? YES. i = 2
  - nums[2]+1 == nums[3] (2+1 == 4)? NO. Inner loop stops.
- start (0) != nums[i] (2). Append "0->2".
- Increment i to 3.

[ FINDING SECOND RANGE ]
- i = 3: start = 4
- Inner loop checks:
  - nums[3]+1 == nums[4] (4+1 == 5)? YES. i = 4
  - nums[4]+1 == nums[5] (5+1 == 7)? NO. Inner loop stops.
- start (4) != nums[i] (5). Append "4->5".
- Increment i to 5.

[ FINDING THIRD RANGE ]
- i = 5: start = 7
- Inner loop checks:
  - i (5) < len(nums)-1 (5)? NO. Inner loop skipped.
- start (7) == nums[i] (7). Append "7".
- Increment i to 6.

[ END ]
- i (6) < len(nums) is False. Outer loop ends.
- Return ["0->2", "4->5", "7"]

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of elements in the array. Because 
  the index `i` is shared and continuously incremented across both the outer and inner 
  loops, we visit each element exactly once.
- Space Complexity: $O(1)$ auxiliary space. We only use a few integer variables (`i`, 
  `start`) to track our position. The space used by the `res` array is typically not 
  counted toward auxiliary space since it is required for the output.
"""

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        i = 0
        
        while i < len(nums):
            # Anchor the start of our new range
            start = nums[i]

            # Fast-forward 'i' as long as the next number is strictly consecutive
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            # If our pointer moved from the start, we have a range
            if start != nums[i]:
                res.append(str(start) + '->' + str(nums[i]))
            # If the pointer didn't move, it's a standalone number
            else:
                res.append(str(nums[i]))
            
            # Move to the start of the next potential range
            i += 1
        
        return res
