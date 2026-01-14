"""
Docstring for 189_Rotate_array


There are two ways one is the obivous way to push the numbers into another array with index i+2 [where 2 =k]

 this takes N space

we can do this with by taking no space.

input:[1,2,3,4,5,6,7] k =3

*revese the array 

 [7,6,5 |,4,3,2,1]
        K
looks close..now reverse the number from start to k and k to end

 [5,6,7 |,1,2,3,4]
        k

output: [5,6,7,1,2,3,4]
 
   
"""




class Solution(object):
    def rotate(self, nums, k):
     k = k% len(nums)
     l,r = 0, len(nums)-1


     while l <r:
        nums[l],nums [r]  = nums[r],nums[l]
        l , r = l+1,r-1

     l, r = 0, k-1
     while l <r:
        nums[l],nums [r]  = nums[r],nums[l]
        l , r = l+1,r-1
     l,r = k, len(nums)-1
     while l <r:
        nums[l],nums [r]  = nums[r],nums[l]
        l , r = l+1,r-1              
## Time O(n)
## Space O(1)


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n

        nums.reverse()

        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])


class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        res = [0]*n

        for i in range(0,n):
            res[(i+k)%n] = nums[i]  

        for i in range(0,n):
            nums[i] = res[i]


#time o(n)
#space O(n)

