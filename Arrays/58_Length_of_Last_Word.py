"""
58. Length of Last Word (Reverse Traversal)
# Most Optimial O(1) space
 --- The Core Intuition ---
1. Start at the End: Since we only care about the *last* word, reading from left to right 
   is a waste of time. We should set a pointer to the very last character of the string.
2. Phase 1 - Skip Trailing Spaces: The string might end with empty spaces (e.g., "hello   "). 
   Our first loop just moves our pointer to the left until we hit a real letter.
3. Phase 2 - Count the Word: Once we find a letter, we start counting. We keep moving left, 
   adding 1 to our length for every letter we see.
4. The Exit Condition: As soon as we hit another space (or reach the very beginning of the 
   string), it means the last word has ended. We break out and return the count.

--- Visual Traversal Walkthrough ---

Example: s = "Hello World  "

[ INITIAL SETUP ]
- Length of s = 13.
- i = 12 (pointing to the last space)
- length = 0

[ PHASE 1: SKIP SPACES ]
- i = 12: s[12] is " ". Move left. (i = 11)
- i = 11: s[11] is " ". Move left. (i = 10)
- i = 10: s[10] is "d". It's not a space! The first loop ends.

[ PHASE 2: COUNT THE WORD ]
- i = 10: s[10] is "d". length = 1. Move left. (i = 9)
- i = 9: s[9] is "l". length = 2. Move left. (i = 8)
- i = 8: s[8] is "r". length = 3. Move left. (i = 7)
- i = 7: s[7] is "o". length = 4. Move left. (i = 6)
- i = 6: s[6] is "W". length = 5. Move left. (i = 5)
- i = 5: s[5] is " ". It IS a space! The second loop ends.

[ END ]
- Return length (5).

--- Complexity ---
- Time Complexity: $O(N)$ in the worst case (if the string is just one giant word, we scan 
  the whole thing). However, in practice, it is usually $O(K)$ where $K$ is the length of 
  the last word plus any trailing spaces. It is much faster than Approach 1 because it 
  halts early.
- Space Complexity: $O(1)$. We are only storing two integer variables (`i` and `length`), 
  requiring zero extra memory regardless of how massive the string is.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # i starts at the very last index. length starts at 0.
        i, length = len(s) - 1, 0

        # Phase 1: Skip over any trailing spaces at the very end of the string
        while s[i] == " ":
            i -= 1
        
        # Phase 2: Count characters until we hit a space or the start of the string
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length



"""
o(n) space 
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Convert the string into a list of words, ignoring all extra spaces
        l = list(s.split()) 
        
        # Return the length of the final word in that list
        return len(l[-1])
