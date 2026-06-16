"""
875. Koko Eating Bananas (Binary Search on Answer)

Koko loves to eat bananas. The 'piles' array represents bananas in different piles, 
and 'h' is the total hours Koko has before the guards return. Koko can eat 'k' 
bananas per hour. If a pile has fewer than 'k' bananas, she finishes it and 
eats nothing else until the next hour. 

--- The Core Intuition: Binary Search on Speed ---
We are looking for the MINIMUM speed 'k' such that Koko finishes all bananas 
within 'h' hours. The speed 'k' can range from 1 (slowest) to the maximum 
number of bananas in any single pile (fastest—eating any more than the largest 
pile size per hour provides no extra benefit).

Since the time taken to eat bananas decreases as speed 'k' increases, the function 
is monotonic. This makes it a perfect candidate for Binary Search!

--- The Math of 'ceil(p/m)' ---
Koko must finish every pile. For a pile of size 'p' and speed 'm', the time 
taken is the ceiling of the division:
$$\text{Hours} = \lceil p / m \rceil$$
Using `math.ceil(p/m)` is the equivalent of integer division `(p + m - 1) // m` 
in programming.



--- Step-by-Step Execution Trace ---

Example: piles = [3, 6, 7, 11], h = 8
Bounds: l = 1, r = 11

--- Iteration 1 ---
- Mid speed (m) = 1 + (11-1)//2 = 6
- Calculate hours: ceil(3/6) + ceil(6/6) + ceil(7/6) + ceil(1/6)
  = 1 + 1 + 2 + 2 = 6 hours.
- 6 <= 8 (Feasible). Save res = 6, try faster: r = m - 1 = 5.

--- Iteration 2 ---
- Mid speed (m) = 1 + (5-1)//2 = 3
- Calculate hours: ceil(3/3) + ceil(6/3) + ceil(7/3) + ceil(11/3)
  = 1 + 2 + 3 + 4 = 10 hours.
- 10 > 8 (Too slow!). Need more speed: l = m + 1 = 4.

--- Iteration 3 ---
- Mid speed (m) = 4 + (5-4)//2 = 4
- Calculate hours: ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4)
  = 1 + 2 + 2 + 3 = 8 hours.
- 8 <= 8 (Feasible). Save res = 4, try faster: r = m - 1 = 3.

Search ends. Result = 4.

--- Complexity ---
- Time Complexity: O(n * log(max(p))), where n is the number of piles and 
  max(p) is the size of the largest pile. We do a binary search on the range of 
  possible speeds, and for each speed, we iterate through all piles.
- Space Complexity: O(1) as we only use pointers and simple variables.
"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The range of possible speeds
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            m = l + (r - l) // 2
            hours = 0
            
            # Calculate total hours required at current speed 'm'
            for p in piles:
                # math.ceil(p / m) tells us how many hours for this specific pile
                hours += math.ceil(p / m)
            
            # If the speed 'm' is sufficient to finish in h hours
            if hours <= h:
                res = m        # This speed is a candidate
                r = m - 1      # Try to see if a slower speed also works
            else:
                # If hours > h, we need to eat faster
                l = m + 1
                
        return res
