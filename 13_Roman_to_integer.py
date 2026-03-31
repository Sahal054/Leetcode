""" 
simple one  the trick is understanding how roman works.

usually a higher value comes first then lower eg 6 = VI(5 +1)

if a lower value comesfirst then we need to subtract eg 4 = IV( 1- 5)

with this logic we add values to res.




"""



class Solution(object):
    def romanToInt(self, s):
        roman = {"I":1,"V" :5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0

        for i in range(len(s)):
            if i+1 <len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res      
        """
        :type s: str
        :rtype: int
        """