"""
347. Top K Frequent Elements (Bucket Sort)

--- The Core Intuition ---
1. The Sorting Bottleneck: A standard dictionary count followed by sorting the keys 
   by their frequencies takes $O(N \log N)$ time. We can do better by realizing a strict 
   boundary: an element can appear at most `N` times (the length of the array).
2. The Bucket Sort Trick: Because frequencies are bounded by `N`, we can create an array 
   called `freq` where the *index* of the array represents the *frequency*, and the 
   *value* at that index is a list of all numbers that appeared that many times.
3. Grouping: We iterate through our frequency dictionary and place every number into 
   its corresponding frequency bucket. 
4. The Reverse Extraction: To get the most frequent elements, we simply read the `freq` 
   array backwards (from the highest possible frequency down to 1). We append elements 
   to our result array and stop the exact moment we hit `k` elements.

--- Visual Traversal Walkthrough ---

Example: nums = [1, 1, 1, 2, 2, 3], k = 2
Array length = 6. Our `freq` array will have size 7 (indices 0 through 6).

[ STEP 1: COUNT FREQUENCIES ]
- counter = {1: 3, 2: 2, 3: 1}

[ STEP 2: POPULATE BUCKETS ]
- freq = [ [], [], [], [], [], [], [] ]
- Process (1: 3): Put '1' into bucket at index 3.
- Process (2: 2): Put '2' into bucket at index 2.
- Process (3: 1): Put '3' into bucket at index 1.
- State of freq: [ [], [3], [2], [1], [], [], [] ]
                     ^    ^    ^
                 Freq 1 Freq 2 Freq 3

[ STEP 3: REVERSE EXTRACTION ]
- Loop 'i' backwards from 6 down to 1:
  - i = 6 to 4: Buckets are empty. Skip.
  - i = 3: Bucket contains [1]. Append 1 to `res`. (res = [1], len = 1)
  - i = 2: Bucket contains [2]. Append 2 to `res`. (res = [1, 2], len = 2)
  - len(res) == k (2 == 2)! We found our top K elements. 
  - Return instantly.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of elements in the array. 
  Counting the elements takes $O(N)$. Grouping them into buckets takes $O(N)$. 
  Iterating backward through the buckets takes $O(N)$ in the worst case. We 
  completely bypass the $O(N \log N)$ sorting step!
- Space Complexity: $O(N)$ to store the `counter` dictionary and the `freq` 
  array of lists, which collectively will never hold more than $N$ unique elements.
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        # Create an array of empty lists. Size is len(nums) + 1 because 
        # a number can appear up to len(nums) times.
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        # 1. Tally the frequencies (manual dictionary count)
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        # 2. Place numbers into buckets based on their frequency count
        for n, c in counter.items():
            freq[c].append(n)
            
        # 3. Read buckets from right to left (highest frequency to lowest)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # Stop immediately once we have gathered k elements
                if len(res) == k:
                    return res
