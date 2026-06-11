class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i , j
# Time Complexity: O(N^2)

# Space Complexity: O(1)                
                
                
"""
1. Two Sum (One-Pass Hash Map Lookup Strategy)

The objective is to find two numbers in an array that add up to a specific target 
number and return their indices. Each input has exactly one solution, and you 
cannot use the same element twice.

--- The Core Intuition: Looking into the Past ---
The naive approach is to use two nested loops to check every single pair of numbers, 
which takes a slow O(n^2) time. 

To optimize this to a single scan, we use a Hash Map (Python dictionary) to remember 
the numbers we have already passed by. As we step through the array:
1. We compute the exact "complement" value we need to hit our goal: 
   diff = target - current_number
2. We instantly check our dictionary: "Have we seen this 'diff' before?"
   - If YES: We have found our pair! We return the index of the previously seen 
     complement and our current index.
   - If NO: We store our current number and its index in the dictionary so that 
     future numbers further down the line can look back and find us.



--- Visual Step-by-Step Layout ---

Example Input: nums = [4, 5, 1, 8], target = 9

Dictionary State (Empty at start): {}

--- Iteration 1 (i = 0) ---
- Current Number (n) = 4
- Calculate complement: diff = 9 - 4 = 5
- Is 5 in our dictionary? No.
- Action: Store 4 with its index 0 -> hashmap = {4: 0}

--- Iteration 2 (i = 1) ---
- Current Number (n) = 5
- Calculate complement: diff = 9 - 5 = 4
- Is 4 in our dictionary? YES! (Stored at index 0)
- Match Found! The code immediately returns: (0, 1)

--- Complexity ---
- Time Complexity: O(n). We traverse the list containing n elements exactly once. 
  Each lookup in the hash map takes constant O(1) time.
- Space Complexity: O(n). In the worst-case scenario, we might have to store up 
  to n elements in the dictionary if the matching pair is at the very end of the array.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keeps track of { number_value : index_location }
        hashmap = {}

        # enumerate gives us both the index (i) and the actual value (n)
        for i, n in enumerate(nums):
            diff = target - n 
            
            # Check if the matching piece to our puzzle is already in our history
            if diff in hashmap:
                # Return the index of the complement, followed by the current index
                return [hashmap[diff], i]
            
            # If not found, save the current number and index for future lookups
            hashmap[n] = i

        # The problem guarantees a solution, but returning an empty list serves as a safety fallback
        return []

# Time Complexity: O(N)

# Space Complexity: O(N) 
