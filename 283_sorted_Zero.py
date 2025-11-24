class Solution(object):
    def moveZeroes(self, nums):
        l =0

        for r in range(0,len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r],nums[l]
                l+=1

# - Time complexity: O(n)
# - Space complexity: O(1)

# nums.sort(key=lambda x: x == 0)