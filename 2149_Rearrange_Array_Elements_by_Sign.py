class Solution(object):
    def rearrangeArray(self, nums):
        positive =[]
        negetive =[]
        res =[]

        for i in nums:
            if i<0:
                negetive.append(i)
            else:
                positive.append(i)
        for num1,num2 in zip (positive,negetive):
            res.append(num1)
            res.append(num2)
        return res  
    
# Time complexity (O(n))
# space complexity (O(n))    