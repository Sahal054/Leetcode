"""
921. Minimum Add to Make Parentheses Valid (Greedy / Balance Simulation)

The objective is to find the minimum number of parentheses (either '(' or ')') 
that must be added to make the input string valid. Instead of using an explicit 
Stack data structure which consumes O(N) space, this approach uses simple integer 
counters to track the balance of parentheses in a single pass, achieving O(1) space.

--- The Core Intuition ---
A string of parentheses is valid if:
1. Every opening parenthesis '(' has a matching closing parenthesis ')'.
2. Parentheses are closed in the correct order (you can't close a parenthesis 
   before opening one).

We use two variables to track unmatched parentheses dynamically:
- open_cnt: Counts the number of opening '(' that are currently waiting for a matching ')'.
- close: Counts the number of closing ')' that appeared without any preceding '(' to match them. 
  These ')' are permanently unmatched and will definitely need an added '(' to become valid.



--- Visual Balancing Mechanism ---

Example Input: s = "()))(("

    (   )   )   )   (   (
   --- --- --- --- --- ---
    1   2   3   4   5   6  <- Index

- At Index 1 '(': open_cnt increments to 1.
- At Index 2 ')': Matches the open '('. open_cnt drops back to 0. (Valid pair!)
- At Index 3 ')': No open '(' left to match it! open_cnt falls below 0. 
                  We lock this in as a permanent error (close += 1) and reset open_cnt to 0.
- At Index 4 ')': Another unmatched closing brace. close += 1.
- At Index 5 & 6 '(': Two opening braces pile up waiting for pairs. open_cnt becomes 2.

At the end, we must fix both types of errors:
Total Additions = close (unmatched closures) + open_cnt (leftover unclosed openings)

--- Step-by-Step Code Trace (s = "()))((") ---

Initialization:
open_cnt = 0
close = 0

--- Iteration 1 (c = '(') ---
- open_cnt += 1 -> open_cnt = 1

--- Iteration 2 (c = ')') ---
- open_cnt -= 1 -> open_cnt = 0
- open_cnt < 0 is False.

--- Iteration 3 (c = ')') ---
- open_cnt -= 1 -> open_cnt = -1
- open_cnt < 0 is True:
    - open_cnt = 0
    - close += 1 -> close = 1

--- Iteration 4 (c = ')') ---
- open_cnt -= 1 -> open_cnt = -1
- open_cnt < 0 is True:
    - open_cnt = 0
    - close += 1 -> close = 2

--- Iteration 5 (c = '(') ---
- open_cnt += 1 -> open_cnt = 1

--- Iteration 6 (c = '(') ---
- open_cnt += 1 -> open_cnt = 2

Loop ends. 
Return close + open_cnt -> 2 + 2 = 4

Final Output: 4

--- Complexity ---
- Time Complexity: O(N) where N is the length of the string, as we loop through 
  the characters exactly once.
- Space Complexity: O(1) because we only store two scalar integer counters 
  regardless of string length.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # open_cnt tracks unmatched '('
        # close tracks unmatched ')' that appeared prematurely
        open_cnt = 0
        close = 0

        for c in s:
            if c == "(":
                open_cnt += 1
            else:
                # A ')' cancels out one waiting '('
                open_cnt -= 1
                
                # If open_cnt drops below 0, we have an unmatchable ')'
                if open_cnt < 0:
                    open_cnt = 0  # Reset balance for future pairs
                    close += 1    # Record a permanent unmatched closing brace
                    
        # Total additions needed = missing openings + missing closures
        return close + open_cnt
