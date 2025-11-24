from typing import Counter


class Solution(object):
    def singleNumber(self, nums):
        s = Counter(nums)
    

        for num, cnt in s.items():
            if cnt == 1:
                return num
# Time complexity: O(n)
# Space complexity: O(n)

#or if Counter not allowed 

class Solution(object):
    def singleNumber(self, nums):
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i]  =1  

        print(hashmap)        
    

        for num, cnt in hashmap.items():
            if cnt == 1:
                return num
            




class Solution(object):
    def singleNumber(self, nums):
        for i in range (len(nums)):
            num = nums[i]
            cnt = 0

            for j in range(len(nums)):
                if nums[j] == num:
                    cnt +=1

            if cnt ==1:
                return num        

# brute force
# - Time complexity: O(n^2)
# - Space complexity: O(1)


class Solution(object):
    def singleNumber(self, nums):
        res = 0

        for i in nums:
            res = i ^ res
        return res  

# Time complexity: O(n)
# Space complexity: O(1)    
