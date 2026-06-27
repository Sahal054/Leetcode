"""
219. Contains Duplicate II (Sliding Window & Hash Set)

The objective is to determine if there are two identical numbers in the array that 
are situated no more than 'k' indices apart (i.e., abs(i - j) <= k). 

Instead of using a nested loop to check every possible pair (which would result in 
a slow O(n^2) time complexity), this solution uses a "Sliding Window" combined with 
a Hash Set to achieve O(n) time complexity. 

--- The Core Intuition ---
1. The Window: We maintain a sliding window of elements using a Hash Set (`window`). 
   A Hash Set allows us to check if a number exists in O(1) constant time.
2. The Size Limit: The maximum distance allowed between duplicates is `k`. Therefore, 
   our window should never contain more than `k + 1` elements. 
3. Sliding the Left Bound: We iterate through the array with a right pointer (`r`). 
   If the distance between `r` and our left pointer (`l`) becomes strictly greater 
   than `k`, the element at `l` is now too far away to be a valid duplicate pair. 
   We remove `nums[l]` from the set and shrink the window by moving `l` forward.
4. Duplicate Check: After ensuring the window is the correct size, we simply check 
   if `nums[r]` is already in our set. If it is, we found a match!

--- Visual Traversal Walkthrough ---

Example Array: nums = [1, 2, 3, 4, 2], k = 3

[ INITIAL SETUP ]
window = {}
l = 0

[ ITERATION 1: r=0 ]
- Current number: 1
- Check Window Size: r - l (0 - 0) = 0. Is 0 > 3? No.
- Check Duplicate: Is 1 in window? No.
- Action: Add 1 to window.
  State: l = 0 | window = {1}
  
[ ITERATION 2: r=1 ]
- Current number: 2
- Check Window Size: r - l (1 - 0) = 1. Is 1 > 3? No.
- Check Duplicate: Is 2 in window? No.
- Action: Add 2 to window.
  State: l = 0 | window = {1, 2}

[ ITERATION 3: r=2 ]
- Current number: 3
- Check Window Size: r - l (2 - 0) = 2. Is 2 > 3? No.
- Check Duplicate: Is 3 in window? No.
- Action: Add 3 to window.
  State: l = 0 | window = {1, 2, 3}

[ ITERATION 4: r=3 ]
- Current number: 4
- Check Window Size: r - l (3 - 0) = 3. Is 3 > 3? No. 
  (Distance is exactly k, so it's still valid)
- Check Duplicate: Is 4 in window? No.
- Action: Add 4 to window.
  State: l = 0 | window = {1, 2, 3, 4}

[ ITERATION 5: r=4 ]
- Current number: 2
- Check Window Size: r - l (4 - 0) = 4. Is 4 > 3? YES!
  -> The distance between index 0 and 4 is too large. 
  -> Remove nums[l] (1) from window. window becomes {2, 3, 4}
  -> Increment l by 1. l is now 1.
- Check Duplicate: Is 2 in window? YES! (The window is currently {2, 3, 4})
  -> We found a duplicate! 
  -> Return True.

Final Return: True

--- Complexity ---
- Time Complexity: O(n) where n is the length of `nums`. We traverse the array exactly 
  once. Adding, removing, and looking up items in a Hash Set takes O(1) time on average.
- Space Complexity: O(min(n, k)) because our Hash Set will grow to a maximum size of 
  `k + 1` elements before we start removing the oldest elements.
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # The set stores elements currently inside our sliding window
        window = set()
        
        # 'l' tracks the left boundary of our valid window
        l = 0

        # 'r' represents the right boundary, iterating through every element
        for r in range(len(nums)):
            
            # If the distance between right and left pointers exceeds k,
            # the window is too large. We must shrink it from the left.
            if (r - l) > k:
                window.remove(nums[l])
                l += 1
                
            # If the current number is already in our valid window, we found a pair!
            if nums[r] in window:
               return True
               
            # Otherwise, add the current number to the window and continue
            window.add(nums[r])
            
        # If the loop finishes without finding any pairs within distance k
        return False
