class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefix =  {0:-1}
        total = 0

        for i , n in enumerate(nums):
            total += n
            reminder = total %k
            if reminder not in prefix:
                prefix[reminder] = i

            elif i - prefix[reminder] >1:
                return True    

        return False    