class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[l] = nums[i]
                l+=1
        return l               
#O(n)