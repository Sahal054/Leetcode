"""
Docstring for 283_sorted_Zero
 The logic is relativly simple,
  we use 2 pointers. if a number is a number that is not 0 u swap it with L and then you incriment L

        [0,1,0,3,12]
         L  R
        [1,0,0,3,12]
           L R
        [1,0,0,3,12]
           L   R
        [1,3,0,0,12]   
             L    R
        [1,3,12,0]
              L,R     
"""

class Solution(object):
    def moveZeroes(self, nums):
        l =0

        for r in range(0,len(nums)):
            if nums[r]: # or nums[r] !=0
                nums[l], nums[r] = nums[r],nums[l]
                l+=1

# - Time complexity: O(n)
# - Space complexity: O(1)

# nums.sort(key=lambda x: x == 0)