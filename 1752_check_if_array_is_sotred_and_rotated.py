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