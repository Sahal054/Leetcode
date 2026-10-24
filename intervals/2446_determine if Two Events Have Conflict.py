"""
2446. Determine if Two Events Have Conflict (String Comparison / Interval Overlap)

--- The Core Intuition ---
1. The Lexicographical Cheat Code: Because the times are strictly formatted as `HH:MM` 
   with leading zeros (e.g., `"01:30"`, `"14:00"`), standard alphabetical string comparison 
   perfectly matches chronological time comparison. `"01:30" < "14:00"` evaluates to 
   `True` natively in Python. We do not need to parse these into integers or `datetime` objects!
2. The Universal Overlap Formula: This is the golden rule of 1D intervals. Two intervals 
   `[start1, end1]` and `[start2, end2]` will ALWAYS overlap if:
   - Event 1 starts before (or exactly when) Event 2 ends (`start1 <= end2`) AND
   - Event 2 starts before (or exactly when) Event 1 ends (`start2 <= end1`).
3. The Condition: If both of these conditions are true, a conflict exists. If even one 
   is false, they are completely separated on the timeline.

--- Visual Traversal Walkthrough ---

Example 1: event1 = ["01:15", "02:00"], event2 = ["02:00", "03:00"]

[ APPLYING OVERLAP FORMULA ]
- start1 = "01:15", end1 = "02:00"
- start2 = "02:00", end2 = "03:00"
- Check 1: Is start1 ("01:15") <= end2 ("03:00")? YES.
- Check 2: Is start2 ("02:00") <= end1 ("02:00")? YES.
- Result: Conflict detected! (They touch exactly at "02:00").

Example 2: event1 = ["10:00", "11:00"], event2 = ["14:00", "15:00"]

[ APPLYING OVERLAP FORMULA ]
- start1 = "10:00", end1 = "11:00"
- start2 = "14:00", end2 = "15:00"
- Check 1: Is start1 ("10:00") <= end2 ("15:00")? YES.
- Check 2: Is start2 ("14:00") <= end1 ("11:00")? NO! 
- Result: No conflict. (Event 2 happens entirely after Event 1).

--- Complexity ---
- Time Complexity: $O(1)$. We are performing exactly two string comparisons. Since the 
  strings are always exactly 5 characters long (`HH:MM`), this operates in constant time.
- Space Complexity: $O(1)$ auxiliary space. We don't allocate any extra memory.
"""

class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        # event1[0] is start1, event1[1] is end1
        # event2[0] is start2, event2[1] is end2
        
        # The universal interval overlap check
        return event1[0] <= event2[1] and event2[0] <= event1[1]
