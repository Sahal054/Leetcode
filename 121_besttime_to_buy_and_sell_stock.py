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