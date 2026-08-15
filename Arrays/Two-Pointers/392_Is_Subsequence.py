"""
392. Is Subsequence (Two Pointers / Greedy)

--- The Core Intuition ---
1. The Two Pointer Technique: We need to verify if string `s` exists inside string `t` 
   while maintaining the original relative order. We use one pointer (`i` in the loop) 
   to sweep through `t`, and a second pointer (`sp`) to track our progress in `s`.
2. The Greedy Match: The moment we see a character in `t` that matches the character 
   we are currently looking for in `s`, we greedily accept it. We advance our `sp` 
   pointer to look for the next character. 
3. Why Greedy Works: If we are looking for 'a' and we find it, there is no mathematical 
   benefit to skipping it and hoping to find a "better" 'a' later. Taking the first 
   available match leaves the maximum possible remaining characters in `t` to match 
   the rest of `s`.
4. Bounds Checking: Because `t` might be much longer than `s`, we might find all of `s` 
   before the loop finishes. The check `sp != end` (or `sp < len(s)`) ensures we don't 
   accidentally try to check `s[sp]` after we've already found the whole word, which 
   would cause an IndexError.

--- Visual Traversal Walkthrough ---

Example: s = "abc", t = "ahbgdc"

[ INITIAL SETUP ]
- s is not empty.
- sp = 0 (Looking for 'a')
- end = 3
- Loop `i` iterates through "ahbgdc"

[ i = 0, t[i] = 'a' ]
- Does t[0] ('a') == s[sp] ('a')? YES!
- sp increments to 1. (Now looking for 'b')

[ i = 1, t[i] = 'h' ]
- Does t[1] ('h') == s[sp] ('b')? No. Do nothing.

[ i = 2, t[i] = 'b' ]
- Does t[2] ('b') == s[sp] ('b')? YES!
- sp increments to 2. (Now looking for 'c')

[ i = 3, t[i] = 'g' ]
- Does t[3] ('g') == s[sp] ('c')? No. Do nothing.

[ i = 4, t[i] = 'd' ]
- Does t[4] ('d') == s[sp] ('c')? No. Do nothing.

[ i = 5, t[i] = 'c' ]
- Does t[5] ('c') == s[sp] ('c')? YES!
- sp increments to 3. 

[ END ]
- Loop finishes. 
- Is sp (3) == end (3)? Yes! Return True.

--- Complexity ---
- Time Complexity: $O(T)$ where $T$ is the length of string `t`. We do a single pass 
  through the target string. (Note: A tiny optimization would be to immediately 
  `return True` inside the loop the moment `sp == end`, skipping the rest of `t`).
- Space Complexity: $O(1)$. We are only storing a couple of integer variables (`sp`, `end`), 
  requiring constant extra space regardless of string sizes.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edge case: an empty string is technically a subsequence of any string
        if not s:
            return True 
        
        # 'sp' tracks the index of the character we are currently looking for in 's'
        sp = 0
        end = len(s)
        
        # Iterate through every character in the larger string 't'
        for i in range(len(t)):
            
            # 1. Ensure we haven't already found all characters (sp != end)
            # 2. Check if the current character in 't' matches our target character in 's'
            if sp != end and t[i] == s[sp]:
                # Match found! Move the 's' pointer forward to look for the next character
                sp += 1
        
        # If our 's' pointer successfully reached the end of 's', we found all characters
        return True if sp == end else False
