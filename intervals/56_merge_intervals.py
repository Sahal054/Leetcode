"""
56. Merge Intervals (Sorting / Array Scan)

--- The Core Intuition ---
1. The Sorting Prerequisite: If intervals are unsorted, finding overlaps requires checking 
   every interval against every other interval (an $O(N^2)$ nightmare). By sorting the 
   intervals based on their starting times, we mathematically guarantee that any intervals 
   capable of overlapping will be strictly adjacent to one another in the list.
2. The Anchor (Output Array): We seed our `output` array with the very first interval. 
   This acts as our "anchor." Instead of modifying the original array, we just compare 
   incoming intervals against the very last interval sitting in our `output`.
3. The Overlap Condition: An overlap happens if the `start` time of the incoming interval 
   is less than or equal to the `end` time of our anchor (`lastend`). 
4. The Merge (Max End): When an overlap occurs, we cannot just blindly adopt the incoming 
   interval's end time. Consider `[1, 5]` and `[2, 3]`—the first interval completely 
   swallows the second. Therefore, the new boundary must be the `max()` of both endings.

--- Visual Traversal Walkthrough ---

Example: intervals = [[2, 6], [1, 3], [15, 18], [8, 10]]

[ INITIAL SETUP ]
- Sort intervals by start time: [[1, 3], [2, 6], [8, 10], [15, 18]]
- Seed the output array: output = [[1, 3]]

[ PROCESSING INTERVAL: [2, 6] ]
- start = 2, end = 6
- lastend = output[-1][1] = 3
- Is start (2) <= lastend (3)? YES. Overlap detected!
- output[-1][1] = max(3, 6) = 6
- State of output: [[1, 6]]

[ PROCESSING INTERVAL: [8, 10] ]
- start = 8, end = 10
- lastend = output[-1][1] = 6
- Is start (8) <= lastend (6)? NO. The chain is broken.
- Append new interval to output.
- State of output: [[1, 6], [8, 10]]

[ PROCESSING INTERVAL: [15, 18] ]
- start = 15, end = 18
- lastend = output[-1][1] = 10
- Is start (15) <= lastend (10)? NO. 
- Append new interval to output.
- State of output: [[1, 6], [8, 10], [15, 18]]

[ END ]
- Loop finishes. Return output.

--- Complexity ---
- Time Complexity: $O(N \log N)$ where $N$ is the number of intervals. The single `for` 
  loop is a highly efficient $O(N)$ linear scan, but the initial sorting step dominates 
  the overall time complexity.
- Space Complexity: $O(N)$ to store the `output` array in the worst-case scenario where 
  no intervals overlap at all. (Additionally, the sorting algorithm itself typically 
  requires $O(\log N)$ to $O(N)$ auxiliary space depending on the language's implementation).
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort intervals based on the starting value
        intervals.sort(key=lambda i: i[0])
        
        # Seed the output array with the first interval
        output = [intervals[0]]

        # Iterate through the rest of the intervals
        for start, end in intervals[1:]:
            lastend = output[-1][1]

            # Overlap condition: Does this interval start before the last one ended?
            if start <= lastend:
                # Merge them by stretching the end time if necessary
                output[-1][1] = max(lastend, end)
            else:
                # No overlap, so safely add it as a new distinct interval
                output.append([start, end])
        
        return output
