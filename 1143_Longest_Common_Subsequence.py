"""
1143. Longest Common Subsequence (2D Dynamic Programming)

The goal is to find the length of the longest subsequence common to text1 and text2. 
This solution uses a bottom-up 2D Dynamic Programming table, iterating backward 
from the end of both strings to the beginning.

--- The Core Intuition & Recurrence Relation ---
We build a grid of size (len(text1) + 1) x (len(text2) + 1). 
The extra row and column act as base cases representing empty string boundaries (filled with 0).

At any given cell dp[i][j]:
1. If characters MATCH (text1[i] == text2[j]):
   We found 1 common character! Move diagonally down-right to look at the remaining suffixes.
   Formula: 1 + dp[i+1][j+1]

2. If characters MISMATCH (text1[i] != text2[j]):
   We must drop a character. We check the best outcome of either dropping the current 
   character of text1 (moving down) or text2 (moving right) and take the maximum.
   Formula: max(dp[i+1][j], dp[i][j+1])

$$dp[i][j] = \begin{cases} 1 + dp[i+1][j+1] & \text{if } \text{text1}[i] == \text{text2}[j] \\ \max(dp[i+1][j], dp[i][j+1]) & \text{otherwise} \end{cases}$$

--- Visual 2D Grid Layout (text1 = "abcde", text2 = "ace") ---

As illustrated in the NeetCode screenshot, we iterate from bottom-right to top-left:

          text2 (j) ->
              a     c     e    ""
           +-----+-----+-----+-----+
         a |  3  |  2  |  1  |  0  |  <- Final Answer is at dp[0][0]
           +-----+-----+-----+-----+
         b |  2  |  2  |  1  |  0  |
   t       +-----+-----+-----+-----+
   e     c |  2  |  2  |  1  |  0  |
   x       +-----+-----+-----+-----+
   t     d |  1  |  1  |  1  |  0  |
   1       +-----+-----+-----+-----+
         e |  1  |  1  |  1  |  0  |  <- e matches e: 1 + diagonal (0) = 1
   (i)     +-----+-----+-----+-----+
  |     "" |  0  |  0  |  0  |  0  |  <- Base case boundary
  V        +-----+-----+-----+-----+


--- Step-by-Step Traversal Highlights ---

- Processing Row 'e' (i=4) vs Row 'e' (j=2):
  Characters match! ('e' == 'e') -> dp[4][2] = 1 + dp[5][3] (diagonal 0) = 1

- Processing Row 'b' (i=1) vs Column 'c' (j=1):
  Mismatch ('b' != 'c') -> dp[1][1] = max(dp[2][1] (bottom: 2), dp[1][2] (right: 1)) = 2

- Processing Row 'a' (i=0) vs Column 'a' (j=0):
  Characters match! ('a' == 'a') -> dp[0][0] = 1 + dp[1][1] (diagonal 2) = 3

--- Complexity ---
- Time Complexity: O(M * N) where M = len(text1) and N = len(text2). Every cell is evaluated once.
- Space Complexity: O(M * N) to store the 2D matrix.
"""

from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D matrix initialized with 0s
        # Dimensions: (len(text1) + 1) rows x (len(text2) + 1) columns
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Iterate backwards through both strings
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If characters match, take diagonal cell value and add 1
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # If they mismatch, take the maximum of bottom or right neighbor
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                    
        # The top-left cell stores the length of the longest common subsequence
        return dp[0][0]
