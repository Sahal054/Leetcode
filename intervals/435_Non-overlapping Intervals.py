"""
435. Non-overlapping Intervals (Greedy / Interval Scheduling)

--- The Core Intuition ---
1. The Greedy Choice: When two intervals overlap, we are forced to delete one of them. 
   But which one? The greedy strategy tells us to always delete the interval that ends 
   LATER. By keeping the interval that ends EARLIEST, we leave the maximum possible 
   room on the timeline for future intervals to fit in without overlapping.
2. The Sort: By sorting the intervals (which defaults to sorting by start time), we 
   guarantee we are evaluating them chronologically from left to right.
3. Tracking the Anchor: We don't need to actually physically remove items from the list. 
   We just maintain a `prevEnd` variable that represents the end time of the last 
   interval we safely decided to *keep*.
4. The `min()` Logic: If a new interval overlaps with our kept interval, we increment 
   our removal counter (`res += 1`). Then, we update `prevEnd = min(prevEnd, end)`. 
   This elegantly executes our greedy choice: we "keep" the smaller end time and 
   effectively "erase" the one that stretched further to the right.

--- Visual Traversal Walkthrough ---

Example: intervals = [[1, 2], [2, 3], [1, 3], [3, 4]]

[ INITIAL SETUP ]
- Sort intervals: [[1, 2], [1, 3], [2, 3], [3, 4]]
- res = 0
- Seed anchor: prevEnd = 2  (from the first interval [1, 2])

[ PROCESSING INTERVAL: [1, 3] ]
- start = 1, end = 3
- Is start (1) >= prevEnd (2)? NO. Overlap detected!
- We must erase one. res += 1  (res is now 1).
- Greedy choice: prevEnd = min(2, 3) = 2. 
  (We keep 2. We effectively erased [1, 3] because it stretched further).

[ PROCESSING INTERVAL: [2, 3] ]
- start = 2, end = 3
- Is start (2) >= prevEnd (2)? YES. No overlap!
- It fits perfectly. Update prevEnd = end (3).

[ PROCESSING INTERVAL: [3, 4] ]
- start = 3, end = 4
- Is start (3) >= prevEnd (3)? YES. No overlap!
- It fits perfectly. Update prevEnd = end (4).

[ END ]
- Loop finishes. Return res (1).

--- Complexity ---
- Time Complexity: $O(N \log N)$ where $N$ is the number of intervals. The initial 
  sorting dominates the time. The subsequent `for` loop is a single $O(N)$ linear pass.
- Space Complexity: $O(1)$ auxiliary space (ignoring the space used by the sorting 
  algorithm, which is typically $O(\log N)$ or $O(N)$ depending on the language). We 
  only use a few integer variables (`res`, `prevEnd`).
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort intervals chronologically by start time
        intervals.sort()
        res = 0

        # Anchor the end of the very first interval
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            
            # Case 1: No overlap. The new interval starts after the previous one ends.
            if start >= prevEnd:
                # Keep it, and move our anchor forward
                prevEnd = end
            
            # Case 2: Overlap detected! We are forced to remove one.
            else:
                res += 1
                
                # GREEDY CHOICE: Keep the one that ends first to leave maximum room 
                # for future intervals. We effectively "erase" the longer one.
                prevEnd = min(prevEnd, end)

        return res
