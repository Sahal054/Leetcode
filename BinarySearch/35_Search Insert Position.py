"""
35. Search Insert Position (Linear Scan vs. Binary Search)
Note: This is LeetCode 35 (LeetCode 53 is "Maximum Subarray", though they are close in number!)

--- The Core Intuition ---
1. The Sorted Advantage: The first solution (Linear Scan) is completely valid, but it 
   runs in $O(N)$ time. Because the array is strictly sorted, we can utilize a Binary 
   Search to cut the search space in half at every step, dropping the time to $O(\log N)$.
2. The Midpoint Logic: We maintain a left (`l`) and right (`r`) boundary. We check the 
   middle element. If the target is larger, we know it physically cannot exist in the 
   left half, so we move our left boundary to `mid + 1`. If smaller, we move the right 
   boundary to `mid - 1`.
3. The Magic of 'l' (Left Pointer): The most elegant part of this binary search happens 
   when the target is NOT in the array. The `while` loop terminates exactly when `l > r`. 
   At that exact moment, the `l` pointer has been pushed past every element strictly 
   smaller than the target, meaning it comes to rest on the exact index where the 
   target *should* be inserted.

--- Visual Traversal Walkthrough (Binary Search) ---

Example: nums = [1, 3, 5, 6], target = 2

[ INITIAL SETUP ]
- l = 0, r = 3

[ FIRST ITERATION ]
- mid = 0 + (3 - 0) // 2 = 1  ->  nums[1] is 3
- Is target (2) > nums[mid] (3)? NO. 
- Target must be on the left.
- Update right pointer: r = mid - 1 = 0.

[ SECOND ITERATION ]
- l = 0, r = 0  (They are pointing at the same element)
- mid = 0 + (0 - 0) // 2 = 0  ->  nums[0] is 1
- Is target (2) > nums[mid] (1)? YES.
- Target must be on the right.
- Update left pointer: l = mid + 1 = 1.

[ END ]
- l (1) is now greater than r (0). The loop breaks.
- Return 'l', which is 1. 
- (Inserting 2 at index 1 results in [1, 2, 3, 5, 6], which is perfectly sorted!)

--- Complexity ---
- Solution 1 (Linear): 
  - Time: $O(N)$ to scan the array. Space: $O(1)$.
- Solution 2 (Binary Search): 
  - Time: $O(\log N)$ because the search space halves every iteration. 
  - Space: $O(1)$ auxiliary memory.
"""

class Solution:
    # --- APPROACH 1: Linear Scan (O(N) Time) ---
    def searchInsertLinear(self, nums: list[int], target: int) -> int:
        pos = 0
        
        # Base case checks
        if nums[0] >= target:  # Minor fix: Handles if target is smaller than first element
            return 0
        if target > nums[-1]:
            return len(nums) 
            
        # Scan through looking for the gap
        for i in range(1, len(nums)):
            if nums[i] == target:
                return i
            # Found the gap where the target fits
            elif nums[i-1] < target and nums[i] > target:
                pos = i
                
        return pos 


    # --- APPROACH 2: Binary Search (O(log N) Time) ---
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            # Prevents integer overflow in languages like Java/C++ (good habit!)
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            
            # Target is larger, discard the left half
            if target > nums[mid]:
                l = mid + 1
            # Target is smaller, discard the right half
            else:
                r = mid - 1
                
        # If not found, 'l' lands exactly on the correct insertion index
        return l
