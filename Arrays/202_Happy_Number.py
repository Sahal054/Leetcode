"""
202. Happy Number (HashSet Approach)

--- The Core Intuition ---
1. The Helper Function: `sumOfSquares` rips a number apart digit by digit. It uses 
   `n % 10` to grab the last digit, squares it, adds it to a running total, and then 
   chops the last digit off using integer division `n // 10`.
2. The Memory Set: We create a `visit` set. Every time we calculate a new number, we 
   add it to the set.
3. The Exit Conditions: 
   - If the number becomes 1, we win! Return True.
   - If the number generated is already in our `visit` set, we have entered a cycle. 
     The `while` loop condition `n not in visit` will fail, the loop terminates, and 
     we return False.

--- Visual Traversal Walkthrough ---

Example: n = 2

[ INITIAL SETUP ]
- n = 2, visit = {}

[ LOOP ITERATIONS ]
1. n=2. Add 2 to visit. sumOfSquares(2) -> 4. 
2. n=4. Add 4 to visit. sumOfSquares(4) -> 16.
3. n=16. Add 16 to visit. sumOfSquares(16) -> 1^2 + 6^2 = 37.
4. n=37. Add 37 to visit. sumOfSquares(37) -> 3^2 + 7^2 = 58.
5. n=58. Add 58 to visit. sumOfSquares(58) -> 5^2 + 8^2 = 89.
... (Several steps later) ...
X. n=4. 4 is ALREADY in the visit set! 
- The loop breaks. Return False. 2 is not a happy number.

--- Complexity ---
- Time Complexity: O(log N). The cost of finding the next number is based on the number 
  of digits, which is proportional to log(N). 
- Space Complexity: O(log N). We store every number we generate in the HashSet.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        # Keep going as long as we haven't seen this number before
        while n not in visit:
            visit.add(n)
            
            # If we reach 1, it's a happy number
            if n == 1:
                return True
            
            # Otherwise, generate the next number in the sequence
            n = self.sumOfSquares(n)    
        
        # If the loop breaks, we found a cycle.
        return False
    
    def sumOfSquares(self, n: int) -> int:
        output = 0

        # Rip digits off from right to left
        while n:
            digit = n % 10          # Get the last digit
            digit = digit ** 2      # Square it
            output += digit         # Add to running total
            n = n // 10             # Remove the last digit from n
        return output



"""
202. Happy Number (Fast & Slow Pointers / O(1) Space)

--- The Core Intuition ---
1. The Linked List Analogy: Think of the starting number as the `head` of a linked list, 
   and `sumOfSquare(n)` as the `.next` pointer. 
2. The Tortoise and the Hare: We create two pointers. The `slow` pointer calculates the 
   next number once per step. The `fast` pointer calculates the next number TWICE per step.
3. The Collision: If there is an infinite loop (a cycle), the fast pointer will lap the 
   slow pointer and they will eventually land on the exact same number at the same time. 
4. The Exit: 
   - If the sequence eventually reaches 1, the `fast` pointer will hit 1 first, and 
     the loop terminates.
   - If there is a cycle, `slow` will equal `fast`, the loop terminates, and since `fast` 
     does not equal 1, we know it failed.

--- Visual Traversal Walkthrough ---

Example: n = 2 (We know this cycles through 4, 16, 37, 58, 89...)

[ INITIAL SETUP ]
- slow = 2
- fast = sumOfSquare(2) -> 4

[ LOOP 1 ]
- fast (4) != 1 AND slow (2) != fast (4). We enter loop.
- slow moves 1 step: sumOfSquare(2) -> 4
- fast moves 2 steps: sumOfSquare(sumOfSquare(4)) -> sumOfSquare(16) -> 37

[ LOOP 2 ]
- fast (37) != 1 AND slow (4) != fast (37). We enter loop.
- slow moves 1 step: sumOfSquare(4) -> 16
- fast moves 2 steps: sumOfSquare(sumOfSquare(37)) -> sumOfSquare(58) -> 89

(This continues until fast laps slow inside the cycle and they both equal the same number, e.g., 4).
- The loop breaks because slow == fast.
- Return fast == 1 -> (4 == 1) -> False.

--- Complexity ---
- Time Complexity: O(log N). Same as the HashSet approach, finding the next number 
  takes logarithmic time, and they will collide relatively quickly.
- Space Complexity: O(1). This is why this approach is superior! We only use two integer 
  variables (`slow` and `fast`). We use absolutely zero scaling memory.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        
        # Fast starts one step ahead
        fast = self.sumOfSquare(n)

        # Loop continues as long as fast hasn't reached 1, AND they haven't collided
        while fast != 1 and slow != fast:
            # Slow takes 1 step
            slow = self.sumOfSquare(slow)
            
            # Fast takes 2 steps (nested function call)
            fast = self.sumOfSquare(self.sumOfSquare(fast))
        
        # If loop broke, it's either because fast hit 1, or they collided.
        # Check if it was because we reached the goal.
        return fast == 1

    def sumOfSquare(self, n: int) -> int:
        output = 0 
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        
        return output
