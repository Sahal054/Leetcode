"""
Docstring for 268_missing_number

so there are 2 ways to solve this one is use the xor operator 

when you xor two numsbers if its same u get 0 if not you get 1 ie, 
1 1 0 
1 0 0                                                                   
------
0 1 0


eg 5^5 = 0, 
   4^3 = 1

how so? take  5^5^3 = 3

any number xor 0 is that number
1 0 1  -5
1 0 1  -5
-----
0 0 0
0 1 1  -3
-----
0 1 1 -3


hence we can xor [3,0,1] with [0,1,2,3]  or(len of n)




Option 2 is 

sum[n] - sum[len(n)]  = missing number 

this can be found with eq s = n*(n+1)//2
""" 


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

