class Solution(object):
    def missingNumber(self, nums):
        s = set(nums)
        n = len(nums)

        for i in range(n+1):
            if i not in s:
                return i
            
# time complexity  O(n)  
# space complexity  O(n) 

#most efficent
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        next_sum = n*(n+1)//2

        actual_sum = sum(nums)
        return next_sum - actual_sum
    
# time complexity  O(n)  
# space complexity  O(1))     



#XOR sol
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        res = n

        for i in range (0,n):
            res ^= nums[i]
            res ^=  i 

        return res   

# time complexity  O(n)  
# space complexity  O(1))     

