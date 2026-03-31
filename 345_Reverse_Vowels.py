"""  
we use the two pointer approach.

we inilize l ,r like usual and we keep moving the pointer if its not a vowel. if its a vowel we swap it

    i c e C r e a m 
    L             R

    i c e C r e a m   -> swap  =       a c e C r e i m 
    L           R                         L      R
    
    a c e C r e i m    this goes on until l and r crosses eachother 
        L     R                         

"""


class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)
        l,r = 0,len(s)-1

        while l<r:
            while l<r and s[l] not in vowels:
                l+=1
            while l<r and s[r] not in vowels:
                r-=1
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        return "".join(s)            