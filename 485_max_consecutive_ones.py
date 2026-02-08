"""
Docstring for 485_max_consecutive_ones



relativly simple one 

2 ways one is to use the count method this is self explnatory


the other is to use the window method

[ 1 , 1 , 0 , 1 , 1 , 1 ]
  l   r
[ 1 , 1 , 0 , 1 , 1 , 1 ]  
  l       r

  this is why we use r+1 other wise
          l be here.  
[ 1 , 1 , 0 , 1 , 1 , 1 ]  
              l
              r




"""



class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count  = 0
        mcount =0

        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
            else:
                count =0
            mcount = max(mcount,count) 
        return mcount 
# - Time complexity: O(n)
# - Space complexity: O(1)
# 
# 
# class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l =0
        count =0

        for r in range(0,len(nums)):
            if nums[r] ==0:
                l =r+1
            count = max(count, r-l+1)

        return count        
        """
        :type nums: List[int]
        :rtype: int
        """    
# - Time complexity: O(n)
# - Space complexity: O(1)
        