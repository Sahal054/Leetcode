class Solution(object):
    def maxSubArray(self, nums):

        maxsum = nums[0]
        for i in range(len(nums)):
            asum=0
            for j in range (i,len(nums)):
                asum +=nums[j]
                maxsum = max(maxsum,asum)

        return maxsum  


#Time ComplexityO(n^2)
#Space ComplexityO(1)


class Solution(object):
    def maxSubArray(self, nums):

        maxsum = nums[0]
        currsum =0
        for i in nums:
            if currsum<0:
                currsum =0
            currsum+= i 
            maxsum = max(maxsum, currsum)  
        return maxsum 




# Time ComplexityO(n)
# Space Complexity O(1)
