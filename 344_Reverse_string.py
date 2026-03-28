
""" 
3 ways are there usig 2 pointer , stack and recursion




The intution is simple we use two pointers and we swap the numbers just like that using 2 pointers

"""

class Solution(object):
    def reverseString(self, s):
        l,r = 0,len(s)-1

        while l<r:
            s[r],s[l] = s[l],s[r]
            l+=1
            r-=1    


# this is  using a stack

class Solution(object):
    def reverseString(self, s):

        stack =[]

        for c in s:
            stack.append(c)
        i =0 
        while stack:
            s[i] = stack.pop()
            i+=1


#this is using recursion

class Solution(object):
    def reverseString(self, s):

        def rev(l,r):
            if l<r:
                s[l],s[r] = s[r],s[l]
                rev(l+1,r-1)
        rev(0,len(s)-1)        


