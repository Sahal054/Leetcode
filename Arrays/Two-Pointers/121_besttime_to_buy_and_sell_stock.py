"""
121. Best Time to Buy and Sell Stock (Two Pointers / Sliding Window)

The objective is to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

This problem uses a dynamic sliding window approach via two pointers. The left pointer 
acts as our "buy" day, and the right pointer acts as our "sell" day. 

--- The Core Intuition ---
1. Time Travel is Impossible: We must buy before we can sell. Thus, our left pointer `l` 
   must always come before our right pointer `r`.
2. Tracking the Lowest Price: The `l` pointer's sole job is to sit on the lowest stock 
   price we have seen so far. 
3. Calculating Profit: As the `r` pointer scans forward day by day, we ask: "Is today's 
   price higher than our buy price at `l`?" 
   - If YES: We have a profitable transaction. We calculate the profit and see if it 
     beats our historical maximum (`maxp`).
4. Finding a Better Buy Day: "What if today's price is LOWER than our buy price at `l`?" 
   - If NO (the current price is lower or equal): We have just discovered a brand new 
     lowest price! There is no reason to keep holding onto our old, more expensive buy 
     price. We immediately jump our `l` pointer to the `r` pointer's position.
5. Why this works globally: By instantly abandoning the old buy price when a lower one 
   is found, we guarantee that any future peak will be paired with the absolute lowest 
   possible valley that came before it.

--- Visual Traversal Walkthrough ---

Example: prices = [7, 1, 5, 3, 6, 4]

[ INITIAL SETUP ]
- maxp = 0
- l = 0 (value is 7)
- Loop `r` starts at index 1 and goes to the end.

[ r = 1, value = 1 ]
- Is prices[l] (7) < prices[r] (1)? No.
- We found a cheaper day to buy! 
- Shift `l` to `r`. (l becomes 1).

[ r = 2, value = 5 ]
- Is prices[l] (1) < prices[r] (5)? Yes.
- profit = 5 - 1 = 4. 
- maxp = max(0, 4) = 4.

[ r = 3, value = 3 ]
- Is prices[l] (1) < prices[r] (3)? Yes.
- profit = 3 - 1 = 2. 
- maxp = max(4, 2) = 4 (remains unchanged).

[ r = 4, value = 6 ]
- Is prices[l] (1) < prices[r] (6)? Yes.
- profit = 6 - 1 = 5.
- maxp = max(4, 5) = 5 (new max profit!).

[ r = 5, value = 4 ]
- Is prices[l] (1) < prices[r] (4)? Yes.
- profit = 4 - 1 = 3.
- maxp = max(5, 3) = 5 (remains unchanged).

[ END ]
- Loop finishes. Return maxp (5).

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the length of `prices`. The right pointer `r` 
  iterates through the array exactly one time.
- Space Complexity: $O(1)$. We are only tracking a few integer variables (`l`, `maxp`, 
  `profit`), meaning memory usage remains constant regardless of the array size.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l represents the index of our 'buy' day
        l = 0 
        
        # maxp keeps track of the maximum profit we have seen so far
        maxp = 0

        # r represents the index of our 'sell' day. We start scanning from day 1.
        for r in range(1, len(prices)):
            
            # If the price on our sell day is higher than our buy day, we have a profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                
                # Update maxp if this profit is the highest we've found
                maxp = max(maxp, profit)
            
            # If the price on our sell day is lower (or equal), we found a better day to buy
            else:
                # Instantly shift our buy pointer to this newly found lowest price
                l = r
        
        return maxp










class Solution(object):
    def maxProfit(self, prices):
        maxprice = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]< prices[j]:
                    maxprice = max(maxprice,prices[j]-prices[i])

        return maxprice 

# Time complexity: O(n^2)
# Space Complexity: O(1)    


class Solution(object):
    def maxProfit(self, prices):
        l,r = 0 ,1
        maxprice = 0

        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxprice = max(maxprice,profit)
            else:
                l = r
            r+=1

        return maxprice    



# Time complexity: O(n)
# Space Complexity: O(1)  
