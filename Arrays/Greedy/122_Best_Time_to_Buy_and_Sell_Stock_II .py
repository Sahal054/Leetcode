"""
122. Best Time to Buy and Sell Stock II (Greedy)

The objective is to maximize your profit. Unlike Part I, you can complete as many 
transactions as you like (buy one and sell one share of the stock multiple times), 
but you cannot hold multiple shares at once.

This problem is perfectly solved using a Greedy approach by capturing every single 
positive price movement.

--- The Core Intuition ---
1. Visualizing the Graph: Imagine the stock prices as a line graph. To get the maximum 
   possible profit, you want to capture the height of every single upward slope.
2. The Greedy Choice: We don't need to complexly track the absolute lowest valley and 
   highest peak of a trend. Instead, we just compare today's price with yesterday's price.
3. Capturing Upward Slopes: If today's price is higher than yesterday's, we pretend we 
   bought it yesterday and sold it today, immediately adding the difference to our total 
   profit. 
4. Why this works: Buying on day 1 for $1 and selling on day 3 for $5 (Profit = $4) is 
   mathematically identical to buying on day 1 ($1), selling on day 2 ($3), immediately 
   buying back on day 2 ($3), and selling on day 3 ($5). (Profit = $2 + $2 = $4). By 
   blindly adding every day-to-day increase, we automatically capture the maximum profit 
   of all upward trends.

--- Visual Traversal Walkthrough ---

Example: prices = [7, 1, 5, 3, 6, 4]

[ INITIAL SETUP ]
- profit = 0
- Loop `i` starts at index 1 (value 1) and looks back at `i-1`.

[ i = 1, values: yesterday = 7, today = 1 ]
- Is prices[i-1] (7) < prices[i] (1)? No.
- Price dropped. Do nothing. 
- profit = 0

[ i = 2, values: yesterday = 1, today = 5 ]
- Is prices[i-1] (1) < prices[i] (5)? Yes.
- We capture this upward slope!
- profit += (5 - 1) -> profit is now 4.

[ i = 3, values: yesterday = 5, today = 3 ]
- Is prices[i-1] (5) < prices[i] (3)? No.
- Price dropped. Do nothing.
- profit = 4

[ i = 4, values: yesterday = 3, today = 6 ]
- Is prices[i-1] (3) < prices[i] (6)? Yes.
- We capture this upward slope!
- profit += (6 - 3) -> profit is now 7.

[ i = 5, values: yesterday = 6, today = 4 ]
- Is prices[i-1] (6) < prices[i] (4)? No.
- Price dropped. Do nothing.
- profit = 7

[ END ]
- Loop finishes. Return profit (7).

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the length of `prices`. We iterate through the 
  array exactly once.
- Space Complexity: $O(1)$. We only use a single integer variable (`profit`), so the 
  memory footprint is constant.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # Start from day 1 (index 1) so we can always look back at yesterday (index i-1)
        for i in range(1, len(prices)):
            
            # If today's price is strictly greater than yesterday's price
            if prices[i - 1] < prices[i]:
                # "Buy" yesterday and "sell" today. Add the difference to our total.
                profit += prices[i] - prices[i - 1]
        
        # Return the accumulated profit from all upward price movements
        return profit
