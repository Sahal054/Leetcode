"""
516. Longest Palindromic Subsequence (LCS Mirror Trick)

This problem asks for the length of the longest palindromic subsequence in a string 's'.
Your strategy uses a brilliant reduction trick: The longest palindromic subsequence 
of a string is exactly equal to the Longest Common Subsequence (LCS) between the 
string itself and its REVERSED self!

--- The Core Intuition & Recurrence Relation ---
We build a 2D grid of size (len(s1) + 1) x (len(s2) + 1). 
Unlike the previous backward-looping examples, this code builds the solution 
FORWARD (from top-left to bottom-right).

At any given step for characters s1[i] and s2[j], we populate the NEXT cell dp[i+1][j+1]:
1. If characters MATCH (s1[i] == s2[j]):
   We add 1 to the best subsequence found BEFORE these characters were looked at (diagonal top-left).
   Formula: 1 + dp[i][j]

2. If characters MISMATCH (s1[i] != s2[j]):
   We find the maximum score possible by skipping either the character from s1 (look up) 
   or from s2 (look left).
   Formula: max(dp[i][j+1], dp[i+1][j])

$$dp[i+1][j+1] = \begin{cases} 1 + dp[i][j] & \text{if } s_1[i] == s_2[j] \\ \max(dp[i][j+1], dp[i+1][j]) & \text{otherwise} \end{cases}$$

--- Visual 2D Grid Layout (s = "cbbd", reversed = "dbbc") ---

Because this algorithm loops forward, the base case 0s occupy the TOP row and LEFT column.
The solution dynamically grows towards the bottom-right corner:

          ""    d     b     b     c  (j)
       +-----+-----+-----+-----+-----+
    "" |  0  |  0  |  0  |  0  |  0  |  <- Base case boundaries
       +-----+-----+-----+-----+-----+
     c |  0  |  0  |  0  |  0  |  1  |  <- 'c' matches 'c' at the end
       +-----+-----+-----+-----+-----+
     b |  0  |  0  |  1  |  1  |  1  |
   t   +-----+-----+-----+-----+-----+
   e   |  0  |  0  |  1  |  2  |  2  |  <- Second 'b' locks in a match length of 2
   x   +-----+-----+-----+-----+-----+
   t   |  0  |  1  |  1  |  2  |  2  |  <- Final Answer finishes here! dp[n][m]
   1   +-----+-----+-----+-----+-----+
  (i)
   V



--- 🚨 CRITICAL BUG FIX HIGHLIGHT 🚨 ---
In your previous problems, the loop ran BACKWARDS (`range(len-1, -1, -1)`), which 
concentrated the final answer at the top-left cell `dp[0][0]`.

Because this code loops FORWARD (`range(n)`), the values cascade down to the opposite 
end of the matrix. Returning `dp[0][0]` will always give you 0 because it remains 
untouched! The true answer finishes at the bottom-right cell: `dp[n][m]`.

--- Complexity ---
- Time Complexity: O(n^2) where n is the length of the string.
- Space Complexity: O(n^2) to allocate the 2D grid matrix.
"""

from typing import List

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # The reverse trick: a palindrome read backwards is identical!
        return self.longestsub(s, s[::-1])

    def longestsub(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        
        # Initialize a grid tracking matching combinations
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
   
        # Standard forward iterative loop
        for i in range(n):
            for j in range(m):
                # Characters match -> look diagonally up-left and add 1
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                # Mismatch -> take max of neighbor cell directly above or to the left
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])   
                    
        # FIX: Changed from dp[0][0] to dp[n][m] to collect the forward-accumulated answer
        return dp[n][m]
