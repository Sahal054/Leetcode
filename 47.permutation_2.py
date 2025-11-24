from typing import Counter


class Solution(object):
    def permuteUnique(self, nums):
        sol,res =[],[] 
        hasmap = Counter(nums)


        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])

            for x in hasmap:
                if hasmap[x]>0:
                    sol.append(x)
                    hasmap[x] -=1
                    backtrack()

                    hasmap[x] +=1
                    sol.pop()
        backtrack()
        return res                      

# or 
class Solution(object):
    def permuteUnique(self, nums):
        sol,res =[],[] 
        hasmap = {}

        for i in nums:
            if i in hasmap:
                hasmap[i] +=1
            else:
                hasmap[i] =1 
                    



        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])

            for x in hasmap:
                if hasmap[x]>0:
                    sol.append(x)
                    hasmap[x] -=1
                    backtrack()

                    hasmap[x] +=1
                    sol.pop()
        backtrack()
        return res                      
# - Time complexity: O(n * n!)
# - Space complexity: O(n * n!)

class Solution(object):
    def permuteUnique(self, nums):
        sol = []
        ans =[]
        hashmaps = Counter(nums)

        def backtrack():
            if len(sol) ==len(nums):
                ans.append(sol[:])
            for x in hashmaps:
                if hashmaps[x] >0:
                    sol.append(x)
                    hashmaps[x] -=x
                    backtrack()

                    hashmaps[x] +=1
                    sol.pop()
        backtrack() 
        return ans           
