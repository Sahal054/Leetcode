class Solution(object):
    def isPalindrome(self, s):
        newstr = ""

        for i in s:
            if i.isalnum():
                newstr += i.lower()

        return  newstr == newstr[::-1]          
#time complexity = O(n)    
#space = O(n)
"""
125. Valid Palindrome (Two-Pointer Technique)

The objective is to determine if a string is a palindrome, meaning it reads the 
same forward and backward, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters.

Instead of creating a filtered copy of the string (which takes extra memory), 
this solution uses two pointers converging from both ends toward the center, 
achieving a space complexity of O(1).

--- The Core Intuition ---
- Left pointer (l) starts at index 0 and moves right.
- Right pointer (r) starts at the last index and moves left.
- If a pointer lands on a symbol, space, or punctuation, it skips past it using .isalnum().
- When both pointers land on alphanumeric characters, their lowercase values are compared.



--- Visual Pointer Movement ---

Example String: "a, b; a"

Index:   0    1    2    3    4    5    6
Chars:  [a]  [,]  [ ]  [b]  [;]  [ ]  [a]
         ^                             ^
         l                             r

Step 1: Both 'a' and 'a' are alphanumeric. 
        Compare lowercase: 'a' == 'a' (Match!)
        Move both pointers: l += 1, r -= 1

Index:   0    1    2    3    4    5    6
Chars:  [a]  [,]  [ ]  [b]  [;]  [ ]  [a]
               ^                   ^
               l                   r

Step 2: l is at ',' (not alphanumeric) -> increment l until it finds a letter. -> skips ',' and ' ' -> lands on 'b' (index 3)
        r is at ' ' (not alphanumeric) -> decrement r until it finds a letter. -> skips ' ' and ';' -> lands on 'b' (index 3)

Index:   0    1    2    3    4    5    6
Chars:  [a]  [,]  [ ]  [b]  [;]  [ ]  [a]
                        ^
                       l,r

Step 3: Now l == r (they meet at index 3). The while loop condition `l < r` terminates.
        Return True.

--- Complexity ---
- Time Complexity: O(n) because we traverse the string at most once.
- Space Complexity: O(1) as we modify pointers in place without allocating new strings.
"""

class Solution(object):
    def isPalindrome(self, s):
        # Initialize left and right pointers at both boundaries
        l = 0
        r = len(s) - 1

        while l < r:
            # Shift left pointer to the right if it encounters a non-alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
                
            # Shift right pointer to the left if it encounters a non-alphanumeric character
            while r > l and not s[r].isalnum():
                r -= 1
                
            # Compare character values case-insensitively
            if s[l].lower() != s[r].lower():
                return False
                
            # Move both pointers inward
            l, r = l + 1, r - 1
            
        return True
## Time complexity: O(n)
## Space complexity: O(1)    

class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s)-1

        while  l<r:
            while l<r  and  not self.alphnum(s[l]):
                l +=1
            while r >l and not self.alphnum(s[r]):
                r-=1
            if s[l].lower() !=s[r].lower():
                return False
            l,r = l+1,r-1
        return True

    def alphnum(self,c):
        return(
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c)<= ord('Z')or
            ord('0') <= ord(c)<= ord('9')


        )
