""" 
To solve this we use the method of sliding window.

for each r element is added to the set. if its already present we remove that elemnt and decrease the left pointer.


  a b c a b c b b
  l 
  r

  a b c a b c b b
  l r

  a b c a b c b b  {a,b,c}
  l   r

  a b c a b c b b   -> already in set remove that value  and now{b,c}
  l     r

  a b c a b c b b  -> added a to set{a,b,c}  now found b so set now {a,c}
    l     r

  a b c a b c b b  -> same thing now set {a,b}
      l     r

  a b c a b c b b  -> {a,c}
        l     r


"""





class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charset = set()
        l = 0
        res = 0


        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res = max(res,r-l+1)
        return res
