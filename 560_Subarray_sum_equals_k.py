"""
Docstring for 560_Subarray_sum_equals_k

The intution for the optimum problem is derrived from the brute force solution

consider [1,1,1,1,1] and k = 3

[ 1 , 1 , 1 , 1 , 1]
  |____|
   |_______| - this is 3 so this one is correct

so and so will go on for order of n^2

but if we take a closer look this window already created the answer we need consider

  
 
[ 1 , 1 , 1 , 1 , 1]
 |_____________| -  Take a look at this case here the sum is 4, but if we remove 1 we get our sum

 but doing this for every single element is still On^2  

 solution we use a hasmap to keep the count of the prefix we calulated

 NOTE* we cannot use the sliding window cause there can be negetive values as well 

                                                                               ____
 prefix  count                                                                |    |
   0       1   - initilaized with it cause a sum can be 0 and take the case [1,1,1,1] is a valid option 
   

[ 1 ,-1  ,1  ,1, 1, 1 ]  k =3        
  |____|                 -  sum = 0  hence sum -k = -3   is -3 in the prefix map? then add the prefix to the map      
   

 prefix  count 
   0       2

[ 1 ,-1  ,1  ,1, 1 ,1 ]  k =3        
  |________|       - sum =1, (summ- k) =-2 not in map


 prefix  count 
   0       2
   1       1
   

[ 1 ,-1  ,1  ,1 ,1 , 1]  k =3        
  |____________|  sum = 2 , summ-k = -1 not in map


   prefix  count 
   0       2
   1       1
   2       1


[ 1 ,-1  ,1  ,1 , 1 , 1]  k =3        
  |_______________|  sum = 3 - 3 = 0  is there in pre fix  hence we add 2 to res  
   
   



   
      
   





"""




class Solution(object):
    def subarraySum(self, nums, k):
        count  =0
     

        for i in range (len(nums)):
            sum =0
            for j in range(i,len(nums)):
                sum += nums[j]

                if sum == k:
                    count+=1

        return count     
    
# - Time complexity: O(n^2)
# - Space complexity: O(1)




class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        currSum =0
        prefixSum = {0:1}

        for i in nums: 
            currSum +=i
            diff = currSum -k
            count+= prefixSum.get(diff,0)    
            prefixSum[currSum] = 1+prefixSum.get(currSum,0) 

        return count        









# - Time complexity: O(n)
# - Space complexity: O(n)