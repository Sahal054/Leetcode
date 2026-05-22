"""
5. Longest Palindromic Substring (Expand Around Center Approach)

The objective is to find the longest continuous substring that reads the same 
forward and backward. Instead of using a heavy 2D Dynamic Programming table 
which takes O(N^2) space, this approach uses the highly optimized "Expand 
Around Center" technique, lowering space complexity to a perfect O(1).

--- The Core Intuition ---
Every character (and every space between characters) in a string can be the 
center of a palindrome. We loop through each index and try to expand outwards 
as far as possible by checking if the left and right characters match.

Because palindromes can have two structural shapes, we must check two center types 
for every index 'i':
1. Odd-length Palindromes (e.g., "aba"): The center is a single character. 
   We initialize pointers at the exact same spot: l, r = i, i
2. Even-length Palindromes (e.g., "abba"): The center is between two characters. 
   We initialize pointers side-by-side: l, r = i, i + 1



--- Visual Expansion Diagrams (s = "babad") ---

Example 1: Checking Odd Center at i = 2 (Character 'b')
   Step 1: l, r start at index 2
           l   r
           v   v
       b   a [ b ] a   d      -> Match! ("b") Length = 1

   Step 2: Expand pointers outwards (l -= 1, r += 1)
         l       r
         v       v
       b [ a ] b [ a ] d      -> Match! ("aba") Length = 3 -> New Max!

   Step 3: Expand again
       l           r
       v           v
     [ b ] a   b   a [ d ]    -> Mismatch ('b' != 'd'). Stop expanding.


Example 2: Checking Even Center at i = 1 (l = 1 ('a'), r = 2 ('b'))
         l   r
         v   v
       b [a] [b] a   d        -> Mismatch ('a' != 'b'). Stop immediately.

--- Step-by-Step Code Trace (s = "babad") ---

- i = 0: 
    - Odd center ("b"): Max length 1 -> res = "b"
    - Even center ("ba"): Mismatch.
- i = 1: 
    - Odd center ("bab"): Max length 3 -> res = "bab"
    - Even center ("ab"): Mismatch.
- i = 2: 
    - Odd center ("aba"): Max length 3 -> Already have a length 3 substring.
    - Even center ("ba"): Mismatch.
- i = 3:
    - Odd center ("ada"): Mismatch ('a' != 'd') -> Max length 1.
    - Even center ("ad"): Mismatch.

Final Output: "bab" (or "aba" is also valid!)

--- Complexity ---
- Time Complexity: O(N^2) where N is the length of the string. There are 2N - 1 
  centers, and expanding from each center takes up to O(N) time.
- Space Complexity: O(1) because we only use a few pointer variables instead 
  of an entire allocation table.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # --- 1. ODD LENGTH PALINDROMES ---
            # Center is a single character (e.g., "aba")
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If current palindrome is longer than our previous max
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                # Expand outward
                l -= 1
                r += 1

            # --- 2. EVEN LENGTH PALINDROMES ---
            # Center is between two characters (e.g., "abba")
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If current palindrome is longer than our previous max
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                # Expand outward
                l -= 1
                r += 1
                
        return res
