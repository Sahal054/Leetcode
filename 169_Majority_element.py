from typing import Counter


class Solution(object):
    def majorityElement(self, nums):
        s = Counter(nums)

        for i, v in s.items():
            if v > len(nums)//2:
                return i 
class Solution(object):
    def majorityElement(self, nums):
        hashmap ={}


        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] =1   

        for i, v in hashmap.items():
            if v > len(nums)//2:
                return i 

# Time complexity = O(n)
#Space complexity =O(n)


class Solution(object):
    def majorityElement(self, nums):
        count , res = 0, 0


        for i in nums:
            if  count == 0:
                res = i

            count += (1 if i == res else -1)

        return res 
# Time complexity = O(n)
#Space complexity =O(1)       
    