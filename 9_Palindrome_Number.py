class Solution(object):
    def isPalindrome(self, x):
        res = str(x)[::-1]
        return str(x) == res


x = 123
sol = Solution()
print(sol.isPalindrome(x))

##O(N)    





class Solution(object):
    def isPalindrome(self, x):
        if x <0:
            return False
        check = x    
        res = 0
        while x> 0:
            dight = x%10
            x = x//10
            res = (res*10) + dight
         
        if res == check:
            return True
        else:
            return False       
##o(log(n)) most efficent