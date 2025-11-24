class Solution(object):
    def fourSum(self, nums, target):
        res =[]
        nums.sort()

        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                l = j+1
                r = len(nums)-1

                while l<r:
                    currsum = nums[i] + nums[j] +nums[l] + nums[r]
                    if currsum > target:
                        r-=1
                    elif currsum < target:
                        l+=1
                    else:
                        res.append([nums[i]+nums[j]+nums[l]+nums[r]])
                        l+=1
                        while nums[l] == nums[l-1] and l<r:
                            l+=1
        return res  
    
# - Time complexity: O(n^3)
# - Space complexity: O(n) 

class Solution(object):
    def fourSum(self, nums, target):
        res = []
        quad =[]   
        nums.sort() 

        def ksum(k,start,target):
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    if i> start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    ksum(k-1,i+1,target-nums[i])  
                    quad.pop()
                return     


            l = start
            r = len(nums)-1
            while l<r:
                twosum = nums[l] +nums[r]
                if twosum < target:
                    l+=1
                elif twosum > target:
                    r-=1
                else:
                    res.append(quad +[nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        ksum(4,0,target)                
        return res   
# - Time complexity: approximately O(n^3)
# - Space complexity: approximately O(n