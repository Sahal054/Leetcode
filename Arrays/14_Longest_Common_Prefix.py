"""
14. Longest Common Prefix (Vertical Scanning)

--- The Core Intuition ---
1. Vertical vs. Horizontal: Instead of comparing the first two words entirely, finding their 
   prefix, and then comparing that prefix to the third word (Horizontal Scanning), we use 
   Vertical Scanning. We look at the 1st letter of EVERY word, then the 2nd letter of EVERY 
   word, and so on.
2. The Reference String: We can just use the very first word in the array (`strs[0]`) as our 
   reference. The longest possible common prefix cannot be longer than this first word anyway.
3. The Column Sweep: The outer loop represents the "column" (index `i`) we are currently 
   checking. The inner loop sweeps through every string `s` in the array to check that column.
4. The Two Exit Conditions: We stop scanning and return our result immediately if:
   - `i == len(s)`: We have reached the end of one of the strings (e.g., trying to check 
     the 5th letter of "flow", which doesn't exist).
   - `strs[0][i] != s[i]`: We found a letter that doesn't match our reference string.
5. Accumulation: If the inner loop finishes without triggering an exit condition, it means 
   EVERY string has the exact same letter at index `i`. We add it to `res` and move to the 
   next column.

--- Visual Traversal Walkthrough ---

Example: strs = ["flower", "flow", "flight"]

[ INITIAL SETUP ]
- res = ""
- Reference string: strs[0] = "flower"
- Outer loop `i` will go from 0 to 5 (length of "flower").

[ i = 0 (Checking 1st letter) ]
- s = "flower": index 0 is 'f'. Matches reference 'f'.
- s = "flow":   index 0 is 'f'. Matches reference 'f'.
- s = "flight": index 0 is 'f'. Matches reference 'f'.
* All match! res = "f"

[ i = 1 (Checking 2nd letter) ]
- s = "flower": index 1 is 'l'. Matches reference 'l'.
- s = "flow":   index 1 is 'l'. Matches reference 'l'.
- s = "flight": index 1 is 'l'. Matches reference 'l'.
* All match! res = "fl"

[ i = 2 (Checking 3rd letter) ]
- s = "flower": index 2 is 'o'. Matches reference 'o'.
- s = "flow":   index 2 is 'o'. Matches reference 'o'.
- s = "flight": index 2 is 'i'. MISMATCH! ('o' != 'i')
* Exit triggered. Return res ("fl").

--- Complexity ---
- Time Complexity: $O(N \cdot M)$ where $N$ is the number of strings and $M$ is the length 
  of the shortest string in the array. In the worst case, we do exactly one character 
  comparison for every character in the common prefix across all strings.
- Space Complexity: $O(1)$ auxiliary space. (Though the resulting string `res` takes 
  $O(M)$ space to build and return, we aren't allocating any scaling memory structures 
  like matrices or hashmaps).
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # Use the first string as our reference. Iterate through its indices.
        for i in range(len(strs[0])):
            
            # For the current index 'i', check every single string in the list
            for s in strs:
                
                # Condition 1: If 'i' is out of bounds for the current string 's'
                # Condition 2: If the character doesn't match our reference string
                if i == len(s) or strs[0][i] != s[i]:
                    # We found the breaking point. Return what we have so far.
                    return res
            
            # If we checked every string and didn't return, the character is common!
            res += strs[0][i]
        
        # If we successfully matched the entirety of the first string, return it all
        return res
