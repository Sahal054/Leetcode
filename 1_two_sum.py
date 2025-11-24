class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i , j
# Time Complexity: O(N^2)

# Space Complexity: O(1)                
                
                


class Solution(object):
    def twoSum(self, nums, target):
        hashmap ={}

        for i , n in enumerate(nums):
            diff = target -n

            if diff in hashmap:
                return hashmap[diff],i
            hashmap[n] = i        


# Time Complexity: O(N)

# Space Complexity: O(N) 