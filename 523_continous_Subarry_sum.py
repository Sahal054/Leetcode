"""
523. Continuous Subarray Sum (Prefix Sum Remainder Hashing Strategy)

The objective is to find if the array contains a continuous subarray of at least 
two elements whose sum is a multiple of 'k' (i.e., sum % k == 0).

--- The Core Intuition: The Remainder Match Trick ---
A brute-force check of every subarray takes $O(n^2)$ time. To optimize this to $O(n)$, 
we combine Prefix Sums with a Hash Map and apply modular arithmetic.

If we have two prefix sums, $\text{total}_i$ (sum up to index $i$) and $\text{total}_j$ 
(sum up to index $j$, where $j < i$), the sum of the elements between them is 
$\text{total}_i - \text{total}_j$. 

For this subarray sum to be a multiple of $k$, the following math must hold:
$$(\text{total}_i - \text{total}_j) \pmod k = 0$$
$$\implies \text{total}_i \pmod k = \text{total}_j \pmod k$$

This means if we see the EXACT same remainder twice while scanning the array, the 
elements trapped between those two checkpoints add up to a perfect multiple of 'k'!

--- The Size Constraint Guard ---
The problem specifies that the subarray must have a length of AT LEAST 2. 
To track this, our hash map stores the index where each remainder was *first seen*: 
`{ remainder : first_seen_index }`. 
When we see a repeating remainder at current index `i`, we check if `i - prefix[r] > 1`.

--- Why initialize prefix = {0: -1}? ---
If a prefix sum from the very beginning (index 0) happens to be a multiple of $k$, 
its remainder is 0. By mapping remainder 0 to virtual index -1, a valid subarray 
ending at index $i=1$ will correctly calculate its length as $1 - (-1) = 2$, satisfying 
the size constraint perfectly!

--- Visual Execution Layout ---

Example Input: nums = [23, 2, 4, 6, 7], k = 6
Initial Map: {0: -1}

--- Step-by-Step Execution Trace ---

- i = 0, n = 23:
  total = 23 -> r = 23 % 6 = 5
  5 is not in map. Record it -> prefix = {0: -1, 5: 0}

- i = 1, n = 2:
  total = 23 + 2 = 25 -> r = 25 % 6 = 1
  1 is not in map. Record it -> prefix = {0: -1, 5: 0, 1: 1}

- i = 2, n = 4:
  total = 25 + 4 = 29 -> r = 29 % 6 = 5
  5 IS ALREADY IN MAP! (First seen at index 0)
  Verify length: current_index - first_seen_index -> 2 - 0 = 2
  Since 2 > 1, we have a valid subarray of length 2! (Subarray [2, 4] sums to 6)
  The code immediately returns True.

--- Complexity ---
- Time Complexity: O(n). We traverse the array exactly once. Hash map insertions 
  and lookups take O(1) constant time.
- Space Complexity: O(min(n, k)). In the worst case, the hash map will store at 
  most 'n' unique remainders, bounded by the value of 'k'.
"""

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Map to store { remainder : first_seen_index }
        # Pre-seeded with 0: -1 to handle edge case subarrays starting from index 0
        prefix = {0: -1}
        total = 0      

        for i, n in enumerate(nums):
            total += n
            r = total % k

            # Situation A: This remainder has never been seen before
            if r not in prefix:
                prefix[r] = i  # Store the index of its first appearance

            # Situation B: Remainder seen before! Check if the subarray spans >= 2 elements
            elif i - prefix[r] > 1:
                return True
                
        # If we loop through the entire array without a valid remainder match -> False
        return False
