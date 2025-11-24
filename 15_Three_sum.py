class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i , a in enumerate(nums):
            if i >0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l <r:
                threesum = a + nums[l] +nums[r]
                if threesum > 0:
                    r -=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res                 
#or

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) -1
            while l<r:
                currsum = nums[i] +nums[l] +nums[r]
                if currsum >0:
                    r -=1 
                elif currsum <0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res                 

# Time complexity: O(n^2)
# Space complexity: O(k)