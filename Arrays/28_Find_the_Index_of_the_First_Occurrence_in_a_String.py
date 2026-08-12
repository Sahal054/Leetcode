"""
28. Find the Index of the First Occurrence in a String (Brute Force / Sliding Window)

--- The Core Intuition ---
1. The Search Space Bound: If your haystack is "hello" (length 5) and your needle is "ll" (length 2), 
   you don't need to check starting at index 4 ('o') because there aren't enough letters 
   left to form a 2-letter word. The last valid starting index is 5 - 2 = 3. 
   This is why the outer loop runs exactly `len(haystack) + 1 - len(needle)` times.
2. The Outer Loop (The Starting Line): The variable `i` represents the starting index in 
   the haystack where we are currently attempting to match the needle.
3. The Inner Loop (The Verification): The variable `j` represents our current position 
   inside the needle. We compare `haystack[i + j]` to `needle[j]`. 
4. The Early Exit: If the characters don't match, there is no reason to keep checking 
   the rest of the needle. We `break` the inner loop instantly and move `i` forward.
5. The Success Condition: If we successfully make it to the very last index of the needle 
   (`j == len(needle) - 1`) and the characters match, we have found the entire word! We 
   immediately return the starting index `i`.

--- Visual Traversal Walkthrough ---

Example: haystack = "leetcode", needle = "leeto"

[ INITIAL SETUP ]
- len(haystack) = 8, len(needle) = 5
- Outer loop `i` runs from 0 to (8 + 1 - 5) = 4. 

[ i = 0 (Starting at 'l') ]
- j=0: haystack[0+0] ('l') == needle[0] ('l').
- j=1: haystack[0+1] ('e') == needle[1] ('e').
- j=2: haystack[0+2] ('e') == needle[2] ('e').
- j=3: haystack[0+3] ('t') == needle[3] ('t').
- j=4: haystack[0+4] ('c') != needle[4] ('o'). MISMATCH!
* Break out of inner loop.

[ i = 1 (Starting at 'e') ]
- j=0: haystack[1+0] ('e') != needle[0] ('l'). MISMATCH!
* Break out of inner loop instantly.

[ i = 2, 3, 4 ]
- All immediately fail on j=0 and break.

[ END ]
- Outer loop finishes. Return -1. 

--- Complexity ---
- Time Complexity: $O(N \cdot M)$ where $N$ is the length of the haystack and $M$ is the 
  length of the needle. In the worst-case scenario (e.g., haystack="aaaaaa", needle="aab"), 
  we have to check almost every character of the needle before finding a mismatch, resulting 
  in a quadratic-like runtime.
- Space Complexity: $O(1)$. We are only tracking loop counters (`i` and `j`), requiring 
  zero scaling memory.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Note: 'res' is declared but never actually used in this logic, 
        # so it can be safely removed to clean up the code.
        res = ""

        # Outer loop: 'i' is the starting index in the haystack
        # We stop early if there aren't enough characters left to fit the needle
        for i in range(len(haystack) + 1 - len(needle)):
            
            # Inner loop: 'j' is the current index in the needle
            for j in range(len(needle)):
                
                # If characters don't match, stop checking this starting position
                if haystack[i+j] != needle[j]:
                    break
                
                # If we made it to the last character of the needle without breaking,
                # it means every single character matched!
                if j == len(needle) - 1:
                    return i
        
        # If the outer loop finishes completely, the needle was never found
        return -1
