""" 

same intution  344. reverse a string
"""

#using 2 pointer
class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        l,r = 0,len(w)-1

        while l<r:
            w[l],w[r] = w[r],w[l]
            l+=1
            r-=1
        return  " ".join(w)    

#using stack
class Solution(object):
    def reverseWords(self, s):
        stack =[]
        ans= []

        for w in s.split():
            stack.append(w)
        i =0
        while stack:
            word = stack.pop()
            ans.append(word)
        return " ".join(ans)    
