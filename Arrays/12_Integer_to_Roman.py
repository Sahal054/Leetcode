"""
12. Integer to Roman (Greedy / Math)

--- The Core Intuition ---
1. The Coin Change Analogy: Think of this problem exactly like making change at a cash 
   register. If you owe someone $13, you give them a $10 bill and three $1 bills. You 
   always try to use the largest denominations possible first to minimize the number of bills.
2. The Subtraction Problem: Roman numerals are mostly additive, but they have 6 annoying 
   exceptions where they subtract (e.g., 4 is IV instead of IIII, 9 is IX instead of VIIII). 
3. The Brilliant Hack: Instead of writing complex `if` statements to handle these 6 
   exceptions, we just treat them as their own unique "coins"! We literally add "IV" with 
   a value of 4 directly into our list of available denominations.
4. The Greedy Sweep: We start with our largest coin ("M", 1000) and work our way down. 
   For each coin, we use integer division (`//`) to see exactly how many times it fits into 
   our number. We add that many symbols to our result string, and then we use the modulo 
   operator (`%`) to find the remainder.

--- Visual Traversal Walkthrough ---

Example: num = 3749

[ INITIAL SETUP ]
- res = ""
- Loop through `roman` in reverse order (largest to smallest).

[ val = 1000 ("M") ]
- count = 3749 // 1000 = 3. 
- res += "M" * 3  -> "MMM"
- num = 3749 % 1000 -> 749

[ val = 900 ("CM") ]
- 749 // 900 = 0. Skip.

[ val = 500 ("D") ]
- count = 749 // 500 = 1.
- res += "D" * 1 -> "MMMD"
- num = 749 % 500 -> 249

[ val = 400 ("CD") ]
- 249 // 400 = 0. Skip.

[ val = 100 ("C") ]
- count = 249 // 100 = 2.
- res += "C" * 2 -> "MMMDC C"
- num = 249 % 100 -> 49

[ val = 90 ("XC"), 50 ("L") ]
- Both do not fit into 49. Skip.

[ val = 40 ("XL") ]
- count = 49 // 40 = 1.
- res += "XL" * 1 -> "MMMDC C XL"
- num = 49 % 40 -> 9

[ val = 10 ("X") ]
- 9 // 10 = 0. Skip.

[ val = 9 ("IX") ]
- count = 9 // 9 = 1.
- res += "IX" * 1 -> "MMMDC C XL IX"
- num = 9 % 9 -> 0

[ END ]
- `num` is 0, the remaining values don't fit. Return "MMMDC C XL IX" (without spaces).

--- Complexity ---
- Time Complexity: $O(1)$. This is a strictly bounded operation. The `roman` array has 
  exactly 13 elements. The loop will always run exactly 13 times, regardless of whether 
  the input is 4 or 3999. Because the number of operations never scales with the input size, 
  it is mathematically constant time.
- Space Complexity: $O(1)$. We are storing an array of 13 pairs and a small result string 
  (the maximum possible length is 15 characters for the number 3888). This takes a fixed, 
  tiny amount of memory.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        # Define all base symbols and the 6 subtractive exceptions as fixed mappings
        roman = [["I", 1],
                 ["IV", 4],
                 ["V", 5],
                 ["IX", 9],
                 ["X", 10],
                 ["XL", 40],
                 ["L", 50],
                 ["XC", 90],
                 ["C", 100],
                 ["CD", 400],
                 ["D", 500],
                 ["CM", 900],
                 ["M", 1000]]

        res = ""

        # Iterate backward through the list so we start with the largest value (1000)
        for sym, val in reversed(roman):
            
            # If the current value can fit into our remaining number at least once
            if num // val != 0:
                
                # Calculate exactly how many times it fits
                count = num // val
                
                # Multiply the string symbol by that count and append it (e.g., "C" * 2 = "CC")
                res += (sym * count)
                
                # Shrink our number to just be the leftover remainder
                num = num % val
        
        return res
