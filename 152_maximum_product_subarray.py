class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        maxprod= nums[0]


        for i in range(len(nums)):
            prod =1

            for j in range(i,len(nums)):
                prod *= nums[j]
                maxprod = max(maxprod,prod)
        return maxprod

# - Time Complexity: O(n^2)
# - Space Complexity: O(1)


class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        currMax,currMin = 1,1

        for n in nums:
            if n == 0:
                currMax,currMin = 1,1
                continue 
            temp = currMax*n
            currMax = max(n*currMax,n*currMin,n)     
            currMin = min(temp,n*currMin,n)
            res = max(res,currMax)
        return res   
# - Time Complexity: O(n)
# - Space Complexity: O(1)
