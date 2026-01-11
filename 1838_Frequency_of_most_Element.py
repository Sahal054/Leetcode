"""
Docstring for 1838_Frequency_of_most_Element

The question says frequency or count, we can make the goal as finding the length(1,4,4,4 count =3,lenght =3) to do that we first sort the array so that all the same elements are together.
now all we need to do is find the length. How we do that? intution is to use a sliding window by using a left and a right pointer.
The lenght between the L and right pointer is our answer.

which number we choose and how to find the lenght ?

we are gonna use the right pointer to decide the number we gonna convert in the window. if the right pointer is at 2 then all the elements between L and R will be 2.

num at R * window = sum(window)+k 

so the total number or sum of the window if all the numbers in the window were R, eg 2+2+2+2 =8 , 4*2 =8

we keep a total variable to count the actual total = 1+1+1+2 = 5

we can also add k cause thats our extra 
 5+2 =8

 and vola we have the answer. 


[ 1 ,1 ,1 ,2 ,2 , 4 ] k =2
  L________R
 
"""



class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        res , total =0,0
        l,r =0,0

        while r<len(nums):
            total += nums[r]

            while nums[r]*(r-l+1) > total +k:
                total -= nums[l]
                l+=1

            res = max(res,r-l+1)
            r +=1
        return res     


# Time complexity: O(n log n)
# Space complexity: O(1)    