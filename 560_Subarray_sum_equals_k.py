class Solution(object):
    def subarraySum(self, nums, k):
        count  =0
     

        for i in range (len(nums)):
            sum =0
            for j in range(i,len(nums)):
                sum += nums[j]

                if sum == k:
                    count+=1

        return count     
    
# - Time complexity: O(n^2)
# - Space complexity: O(1)




class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        currSum =0
        prefixSum = {0:1}

        for i in nums: 
            currSum +=i
            diff = currSum -k
            count+= prefixSum.get(diff,0)    
            prefixSum[currSum] = 1+prefixSum.get(currSum,0) 

        return count        









# - Time complexity: O(n)
# - Space complexity: O(n)