#brute force


from typing import Counter


class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        ans ,sol = [],[]
        counts = Counter(nums)

        def backtrack():

            if len(sol) == n:
                ans.append(sol[:])
                return


 
            for num in sorted(counts.keys()):
              
                if counts[num] > 0:
                    sol.append(num)
                    counts[num] -= 1 
                    
                    backtrack()
                    
                    counts[num] += 1 
                    sol.pop()
        

        backtrack()
    

        current_index = ans.index(nums)
        next_index = (current_index + 1) % len(ans) 
        next_p = ans[next_index]
        nums[:] = next_p   


# Time complexity: O(n! * n)
# Space complexity: O(n * n!)




class Solution(object):
    def nextPermutation(self, nums):
        pivot = None
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                pivot = i-1
                break
        else:
            nums.reverse()
            return 

        swap = len(nums) -1 
        while nums[swap] <= nums[pivot]:
            swap -=1

        nums[pivot], nums[swap] = nums[swap],nums[pivot]

        nums[pivot+1:] = reversed(nums[pivot+1:])
        return                   
# Time complexity: O(n)
# Space complexity: O(1)



