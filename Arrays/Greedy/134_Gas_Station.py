"""
134. Gas Station (Greedy Approach)

--- The Core Intuition ---
This solution relies on two massive logical shortcuts:

1. The "Total Sum" Rule: 
   If the total amount of gas across all stations is less than the total cost to 
   travel, it is 100% impossible to complete the circuit. If total gas >= total cost, 
   the problem guarantees a unique solution exists. We check this up front so we don't 
   have to worry about wrapping around the array later.

2. The "Dead Zone" Rule (The Greedy Part):
   Imagine you start at station A and successfully travel through stations B and C, 
   but you run out of gas trying to reach station D. 
   
   Should you try starting at station B next? NO! 
   When you started at A, you arrived at B with *some* gas left over in your tank. 
   Even with that head start, you couldn't reach D. If you start fresh at B with an 
   empty tank, you will definitely fail before D. 
   
   Therefore, if you fail at D, *no station between A and D can be the answer*. 
   You can skip all of them and immediately make station D (or `i + 1`) your new 
   starting candidate.

--- Visual Traversal Walkthrough ---

Example: gas  = [1, 2, 3, 4, 5]
         cost = [3, 4, 5, 1, 2]

[ INITIAL CHECK ]
- sum(gas) = 15, sum(cost) = 15. 15 >= 15, so a solution definitely exists!

[ LOOP ITERATION ]
- start = 0, total = 0

- i=0 (Gas=1, Cost=3): Net = -2. 
  total = -2. It's < 0! We ran out of gas. 
  Reset total = 0, next possible start = 1.

- i=1 (Gas=2, Cost=4): Net = -2. 
  total = -2. It's < 0! We ran out of gas. 
  Reset total = 0, next possible start = 2.

- i=2 (Gas=3, Cost=5): Net = -2. 
  total = -2. It's < 0! We ran out of gas. 
  Reset total = 0, next possible start = 3.

- i=3 (Gas=4, Cost=1): Net = +3.
  total = 3. We made it to the next station!

- i=4 (Gas=5, Cost=2): Net = +3.
  total = 6 (3 from before + 3). We made it!

[ END ]
- Loop finishes. Return `start` which is 3. 
- (Because we verified sum(gas) >= sum(cost) at the very beginning, we don't even 
  need to simulate wrapping around from index 4 back to index 0. The math guarantees 
  index 3 will make it all the way around).

--- Complexity ---
- Time Complexity: $O(N)$. We calculate the sum of the arrays, which takes $O(N)$, 
  and then we do a single `for` loop through the array, which is another $O(N)$. 
  $O(2N)$ simplifies to $O(N)$.
- Space Complexity: $O(1)$. We are only storing two integer variables (`total` and `start`).
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Shortcut 1: If we don't have enough gas overall, it's impossible.
        # This guarantees that if we pass this check, a valid start node exists.
        if sum(gas) < sum(cost):
            return -1
        
        total = 0   # Keeps track of gas in the tank for our current trip attempt
        start = 0   # The station we are currently testing as our starting point

        for i in range(len(gas)):
            # Add gas from current station, subtract cost to get to the next
            total += (gas[i] - cost[i])

            # Shortcut 2: If tank drops below zero, this starting point failed.
            if total < 0:
                # Reset tank to empty for the next attempt
                total = 0
                # Any station from our 'start' up to 'i' is invalid.
                # Try the very next station as the new starting point.
                start = i + 1

        return start
