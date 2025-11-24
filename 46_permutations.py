class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]

        perm = self.permute(nums[1:])
        res =[]
        for p in perm:
            for i in range(len(p) +1):
                p_copy =p[:]
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res 

#this is constructive recursion
# - Time complexity: O(n^2 * n!)
# - Space complexity: O(n * n!)

class Solution(object):
    def permute(self, nums):
        n = len(nums)
        ans ,sol = [],[]

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans                    

#Recursive backtracking