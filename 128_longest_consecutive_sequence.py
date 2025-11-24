class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        count =1
        mcount =1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] ==nums[i-1] +1:
                count+=1
                mcount = max(count,mcount)                    
 
            else:
                count =1
        return mcount   
# - Time complexity: O(n log n)
# - Space complexity: O(n)    

class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        count = 0

        for i in numset:
            if i-1 not in numset:
                next_num = i+1
                longest = 1
                while  next_num in numset:
                    longest +=1
                    next_num +=1
                count = max(count,longest)
        return count  

# - Time complexity: O(n)
# - Space complexity: O(n)        
