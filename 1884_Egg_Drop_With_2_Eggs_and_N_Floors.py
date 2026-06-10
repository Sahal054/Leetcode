"""
1884. Egg Drop With 2 Eggs and N Floors (Math & Optimization Strategy)

The objective is to find the minimum number of drops needed in the worst-case 
scenario to find the highest floor 'f' from which an egg can be dropped without breaking. 
You are given exactly 2 identical eggs and a building with 'n' floors.

--- The Core Intuition: Balancing the Risk ---
If you only had 1 egg, you would have no choice but to start at floor 1 and walk up 
one floor at a time (Linear Search). If you skipped floors, and the egg broke, you 
would never know the exact floor.

With 2 eggs, you can use Egg 1 to take big leaps to narrow down a range, and Egg 2 
to do a linear search within that broken range. 

To minimize the WORST-CASE total drops, we want the total number of drops to remain 
completely constant, regardless of which floor Egg 1 happens to break on. 
- If our target worst-case drops is 'x', we drop Egg 1 from floor 'x'.
- If it breaks, we have used 1 drop and have 1 egg left to check the remaining (x - 1) floors below it. 
  Total drops = 1 + (x - 1) = x.
- If it doesn't break, we have already used 1 drop. For our next leap to maintain the same total 
  worst-case cost 'x', we can only leap ahead by (x - 1) floors. 
- If it breaks there, Egg 2 takes at most (x - 2) drops. Total drops = 1 + 1 + (x - 2) = x.

Therefore, with 'x' drops, the maximum number of floors we can safely test is:
$$x + (x - 1) + (x - 2) + (x - 3) + \dots + 1 \ge n$$

This is a classic arithmetic progression sum:
$$\frac{x(x + 1)}{2} \ge n$$


--- Visual Shifting Interval Example (n = 100) ---
If n = 14 drops is our target:
- Drop 1: Floor 14  (If it breaks, check 1 to 13 -> Max 14 drops)
- Drop 2: Floor 27  (14 + 13) (If it breaks, check 15 to 26 -> Max 14 drops)
- Drop 3: Floor 39  (27 + 12)
- Drop 4: Floor 50  (39 + 11)
...
- Drop 14: Floor 100

--- Complexity ---
- Time Complexity: O(sqrt(n)) because the loop runs roughly sqrt(2n) times.
- Space Complexity: O(1) as we only use a few tracking variables.
"""

class Solution:
    def twoEggDrop(self, n: int) -> int:
        # 'drops' represents the number of drops we are testing out (the 'x' variable)
        drops = 1
        # 'floors_covered' is the total cumulative floors we can check with this many drops
        floors_covered = 0
        
        # Keep adding matching mathematical intervals until we can cover 'n' floors
        while floors_covered < n:
            floors_covered += drops
            
            # If our triangular sum can reach or exceed the building height, we found our answer
            if floors_covered >= n:
                return drops
                
            drops += 1
