"""
135. Candy (Two-Pass Greedy Approach)

--- The Core Intuition ---
1. The Problem with Neighbors: If you try to compare a child's rating to BOTH their 
   left and right neighbors at the same time, you get stuck in a cascading loop. 
   Updating one child's candy might suddenly invalidate the child before them!
2. Divide and Conquer: We break the rule into two simpler rules.
   - Rule A: If I have a higher rating than my LEFT neighbor, I get more candy than them.
   - Rule B: If I have a higher rating than my RIGHT neighbor, I get more candy than them.
3. Pass 1 (Left to Right): We give everyone 1 candy to start. Then, we sweep forward. 
   We ONLY look at the left neighbor. If the current child has a higher rating, we 
   give them exactly 1 more candy than whatever the left neighbor just got.
4. Pass 2 (Right to Left): We sweep backward. We ONLY look at the right neighbor. 
   If the current child has a higher rating, they need more candy than the right neighbor. 
   BUT we can't just blindly assign `right_neighbor + 1`. We must take the `max()` of 
   what they already have (from Pass 1) and what they need now. If we don't use `max()`, 
   we might accidentally take away candies they needed to satisfy the left neighbor!

--- Visual Traversal Walkthrough ---

Example: ratings = [1, 2, 5, 4, 3, 2, 1]  (A massive peak in the middle)

[ INITIAL SETUP ]
- array = [1, 1, 1, 1, 1, 1, 1]

[ PASS 1: Left to Right ]
- i=1 (Rating 2 vs 1): 2 > 1. array[1] = 1 + 1 = 2.   Array: [1, 2, 1, 1, 1, 1, 1]
- i=2 (Rating 5 vs 2): 5 > 2. array[2] = 2 + 1 = 3.   Array: [1, 2, 3, 1, 1, 1, 1]
- i=3 (Rating 4 vs 5): 4 is not > 5. Do nothing.      Array: [1, 2, 3, 1, 1, 1, 1]
- ... (Rest are decreasing, so Pass 1 ignores them)
* After Pass 1: [1, 2, 3, 1, 1, 1, 1] (Only the upward slope is satisfied)

[ PASS 2: Right to Left ]
- i=5 (Rating 2 vs 1): 2 > 1. max(1, 1+1=2) -> 2.     Array: [1, 2, 3, 1, 1, 2, 1]
- i=4 (Rating 3 vs 2): 3 > 2. max(1, 2+1=3) -> 3.     Array: [1, 2, 3, 1, 3, 2, 1]
- i=3 (Rating 4 vs 3): 4 > 3. max(1, 3+1=4) -> 4.     Array: [1, 2, 3, 4, 3, 2, 1]
- i=2 (Rating 5 vs 4): 5 > 4. max(3, 4+1=5) -> 5.     Array: [1, 2, 5, 4, 3, 2, 1] 
  *Notice here at i=2, if we didn't use max(), we might have messed up the peak!*

[ RESULT ]
- sum([1, 2, 5, 4, 3, 2, 1]) = 18 candies.

--- Complexity ---
- Time Complexity: O(N). We iterate through the list exactly twice sequentially. O(2N) 
  simplifies to O(N).
- Space Complexity: O(N). We create a single additional array `array` of size N to 
  store the candy distributions.
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Give every child 1 candy to satisfy the baseline constraint
        array = [1] * len(ratings)

        # PASS 1: Left to Right
        # Check against the left neighbor.
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                # Increment based on left neighbor's candies
                array[i] = array[i-1] + 1 

        # PASS 2: Right to Left
        # Check against the right neighbor.
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # CRITICAL: Take the max so we don't break the rule we established in Pass 1
                array[i] = max(array[i], (array[i+1] + 1))

        # The total is the minimum number of candies required
        return sum(array)
