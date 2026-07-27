"""
274. H-Index (Bucket Sort / Counting)

--- The Core Intuition ---
1. The Cap: The maximum possible H-Index is `n` (the total number of papers). Any paper 
   with more than `n` citations is fundamentally no different than a paper with exactly 
   `n` citations when calculating the H-Index.
2. The Buckets: We create an array `paper_count` of size `n + 1` to act as buckets. 
   Index `x` of this array will store the number of papers that have exactly `x` citations.
3. Filling the Buckets: We iterate through our citations. We increment the corresponding 
   bucket. If a citation is greater than `n`, we cap it and dump it into the last bucket `n`.
4. Working Backwards: We start checking from the highest possible H-Index (`h = n`) and 
   move down. We keep a running total of `papers` we've seen so far from the buckets.
5. The Exit Condition: The moment our accumulated `papers` count becomes greater than 
   or equal to our current `h`, we have found our H-Index! 

--- Visual Traversal Walkthrough ---

Example: citations = [3, 0, 6, 1, 5] 
- n = 5
- Create buckets: paper_count = [0, 0, 0, 0, 0, 0] (Indices 0 through 5)

[ FILLING BUCKETS ]
- cite = 3: paper_count[3] += 1
- cite = 0: paper_count[0] += 1
- cite = 6: Cap at n(5). paper_count[5] += 1
- cite = 1: paper_count[1] += 1
- cite = 5: paper_count[5] += 1
- Resulting buckets: [1, 1, 0, 1, 0, 2] 
  (1 paper with 0, 1 paper with 1, 0 with 2, 1 with 3, 0 with 4, 2 with >= 5)

[ WORKING BACKWARDS ]
- Initialize: h = 5, papers = paper_count[5] = 2.

- While papers (2) < h (5):
  - Decrease h to 4.
  - Add papers from bucket 4 to total: papers = 2 + 0 = 2.

- While papers (2) < h (4):
  - Decrease h to 3.
  - Add papers from bucket 3 to total: papers = 2 + 1 = 3.

- While papers (3) < h (3):
  - Condition is FALSE! 3 is not less than 3. Loop terminates.

[ END ]
- Return h (3).

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of papers. We iterate through the 
  `citations` array once to fill the buckets, and iterate through the buckets once (at most) 
  to find the H-Index.
- Space Complexity: $O(N)$ to store the `paper_count` array which scales linearly 
  with the number of papers.
"""

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        # Create n + 1 buckets. Index represents citation count, value represents number of papers.
        paper_count = [0] * (n + 1)

        # Populate the buckets
        for c in citations:
            # If citations > n, cap it at n. 
            paper_count[min(n, c)] += 1
        
        # Start checking from the maximum possible H-index
        h = n
        
        # Start our running total of valid papers with the highest bucket
        papers = paper_count[n]

        # While our total valid papers is less than the current H-index we are checking
        while papers < h:
            h -= 1                    # Drop the H-index requirement by 1
            papers += paper_count[h]  # Add papers from the next bucket down to our running total
        
        return h




"""
274. H-Index (Brute Force)

--- The Core Intuition ---
1. Understanding the H-Index: A researcher has an H-Index of `h` if they have published 
   at least `h` papers that have each been cited at least `h` times.
2. The Maximum Possible H-Index: The highest possible H-Index a researcher can have is 
   equal to their total number of papers. (If you write 5 papers, your H-Index cannot be 6).
3. The Brute Force Strategy: We test every potential H-Index `i` starting from 1 up to 
   the total number of papers (`len(citations)`). 
4. The Inner Check: For each potential H-Index `i`, we iterate through the entire `citations` 
   array and count how many papers have `i` or more citations. 
5. The Update: If our `count` of valid papers is greater than or equal to `i`, then `i` is 
   a valid H-Index. We update our `maxh` and continue checking higher numbers.

--- Visual Traversal Walkthrough ---

Example: citations = [3, 0, 6, 1, 5] (Total papers = 5)

[ INITIAL SETUP ]
- maxh = 0
- Loop `i` from 1 to 5.

[ i = 1 (Checking for H-Index of 1) ]
- How many papers have >= 1 citation? (3, 6, 1, 5) -> count = 4.
- Is count (4) >= i (1)? Yes. 
- maxh = 1.

[ i = 2 (Checking for H-Index of 2) ]
- How many papers have >= 2 citations? (3, 6, 5) -> count = 3.
- Is count (3) >= i (2)? Yes. 
- maxh = 2.

[ i = 3 (Checking for H-Index of 3) ]
- How many papers have >= 3 citations? (3, 6, 5) -> count = 3.
- Is count (3) >= i (3)? Yes. 
- maxh = 3.

[ i = 4 (Checking for H-Index of 4) ]
- How many papers have >= 4 citations? (6, 5) -> count = 2.
- Is count (2) >= i (4)? No. 
- maxh remains 3.

[ i = 5 (Checking for H-Index of 5) ]
- How many papers have >= 5 citations? (6, 5) -> count = 2.
- Is count (2) >= i (5)? No. 
- maxh remains 3.

[ END ]
- Return maxh (3).

--- Complexity ---
- Time Complexity: $O(N^2)$ where $N$ is the number of papers. For every possible 
  H-Index from 1 to $N$, we iterate through the entire array of size $N$. 
- Space Complexity: $O(1)$. We only use a few variables (`maxh`, `count`), 
  requiring constant extra space.
"""

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxh = 0
        
        # Test every possible H-Index from 1 up to the total number of papers
        for i in range(1, len(citations) + 1):
            count = 0

            # Count how many papers have at least 'i' citations
            for cite in citations:
                if cite >= i:
                    count += 1
            
            # If the number of qualified papers is at least 'i', it's a valid H-Index
            if count >= i:
                maxh = i
        
        return maxh
