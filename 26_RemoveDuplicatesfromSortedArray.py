"""
Docstring for 26_RemoveDuplicatesfromSortedArray

We use a 2 pointer approach for this.

[0,0,1,1,1,2,2,3,3,4]
   L
   R

[0,0,1,1,1,2,2,3,3,4] --> [0,1,_,1,1,2,2,3,3,4] 
   L R                       L  R

the trick is to find all the uniqe elements in the array. this is being done by the L pointer.

we dont replace the same element in R to L instead if replace the UNIQUE element.

we search L and R if L and R is the same R shifts next. IF is not the same then whats at R is shifted to L.

end we return L

"""

class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[l] = nums[i]
                l+=1
        return l               
#O(n)