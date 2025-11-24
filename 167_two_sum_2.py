class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0 , len(numbers) -1
        while l<r:
            sums = numbers[l] +numbers[r] 
            if sums > target:
                r -=1
            elif sums< target :
                l +=1
            else:
                return [l+1, r+1 ]   

#time O[n]
# space O[1]            