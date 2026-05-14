"""
Insert Interval Algorithm

This algorithm inserts a new interval into a sorted list of non-overlapping 
intervals, merging any overlaps that occur. We process the intervals in 
three distinct phases:

1. BEFORE Overlap: Intervals that end before the new interval starts.
2. DURING Overlap: Intervals that overlap with the new interval (they get merged).
3. AFTER Overlap: Intervals that start after the new interval ends.

--- Visual Logic ---


Example: intervals = [[1,2], [3,5], [6,7], [8,10]], newInterval = [4,8]

Step 1: [1,2] is strictly BEFORE the new interval [4,8].
   |--1--2--|      |--4--------8--|
   (Append [1,2] to result)

Step 2: [3,5] overlaps with [4,8].
   |----3-----5----|
         |----4--------8----|
   (Merge: start = min(3,4), end = max(5,8) -> newInterval = [3,8])

Step 3: [6,7] overlaps with [3,8].
         |---6---7---|
   |-----3-----------8-----|
   (Merge: start = min(3,6), end = max(8,7) -> newInterval = [3,8])

Step 4: [8,10] overlaps with [3,8].
                     |--8---10--|
   |-----3-----------8-----|
   (Merge: start = min(3,8), end = max(8,10) -> newInterval = [3,10])

Result: [[1,2], [3,10]]

--- Step-by-Step Trace of Your Code ---

Input: intervals = [[1,3], [6,9]], newInterval = [2,5]

--- Iteration 1 (i=0): interval = [1,3] ---
- Condition 1 (newInterval[1] < 1): 5 < 1? False.
- Condition 2 (newInterval[0] > 3): 2 > 3? False.
- ELSE (Overlap): 
    newInterval = [min(2, 1), max(5, 3)] = [1, 5]

--- Iteration 2 (i=1): interval = [6,9] ---
- Condition 1 (newInterval[1] < 6): 5 < 6? TRUE!
    - Append [1, 5] to res.
    - Return res + intervals[1:] (which is [[1, 5], [6, 9]])

Final Output: [[1,5], [6,9]]
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res= []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        res.append(newInterval) 
        return res    
        
