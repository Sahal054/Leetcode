def check(nums):
        sorted_arry = sorted(nums)
        arry =[]


        for i in range(len(nums)):
            arry.insert(0,sorted_arry.pop())
            if nums == arry + sorted_arry:
                return True

        return False         
  
# Time complexity: # O(n^2)
#Space complexity:O(n) 



"""
now for a solution which is less than O(n^2) 
we are gonna transform this problem into a sliding window. the best way to deal with rotation arrays is to add the array with itself

eg 3,4,5,1,2
becomes -  3,4,5,1,2,3,4,5,1,2
                 L       R
as you can see we have found our answer. but finding the lenght is the issue we cant take the lenght of the R element or something cause all the elements are differnt
fiding the window using two loops is also O(n^2)

now the next solution is simply to check if the number is in ascending order, if the previous number is more than R the  bring L to R

this makes the window souluion.. but it takes extra space we can eliminate that by simply modding that index by the lenght

3 4 5 5 1 2   len = 6  
0 1 2 3 4 5 

                i 
3 4 5 5 1 2 3 4 5 5 1 2 
0 1 2 3 4 5 6 7 8 9 10 11

8%6 = 2 
now we just retrun if the count == len of the array if yes. we have our answer 


"""



def check(self, nums):
        N = len(nums)
        count  =1 
        if N ==1:
            return True

        for i in range(1, 2*N):
            if nums[(i-1) %N] <= nums[i%N]:
                count +=1
            else:
                count =1
            if count == N:
                return True
        return False 
# time: O(n)
# speace :O(1)



class Solution(object):
    def check(self, nums):
        count=0
        for i in range(len(nums)):
            if(nums[i]<nums[i-1]):
                count+=1
        return count<=1