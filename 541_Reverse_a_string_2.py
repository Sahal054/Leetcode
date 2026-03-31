"""

the concept is simple,

from the looop we take 2*k, and reverse the elements till there thats all




 """


class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)

        for i in range(0,len(s),2*k):
            s[i:i+k] = reversed(s[i:i+k])

        return "".join(s)   