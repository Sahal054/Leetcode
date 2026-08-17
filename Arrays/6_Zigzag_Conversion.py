"""
6. Zigzag Conversion (Simulation / Array of Strings)

--- The Core Intuition ---
1. Skip the Math: There is a purely mathematical way to solve this by calculating the 
   exact jump distances between characters. However, that approach is highly prone to 
   off-by-one errors. The much cleaner approach is to just simulate the physical process 
   of writing the zigzag!
2. The Bucket System: We create an array called `store` with `numRows` empty strings. 
   Think of these as buckets representing each horizontal row. 
3. The Bouncing Ball: We read the string character by character and drop them into the 
   buckets. We use a `level` pointer to track which bucket we are currently on, and a 
   `direction` variable (+1 for moving down, -1 for moving up).
4. Changing Direction: Just like a bouncing ball, when our `level` hits the top row (0), 
   gravity pulls it down (`direction = 1`). When it hits the bottom row (`numRows - 1`), 
   it bounces back up (`direction = -1`).
5. The Assembly: After dropping every character into its appropriate row bucket, we 
   simply concatenate all the buckets together into one single string.

--- Visual Traversal Walkthrough ---

Example: s = "PAYPAL", numRows = 3

[ INITIAL SETUP ]
- store = ['', '', '']
- level = 0
- direction = 1

[ Char 1: 'P' ]
- store[0] += 'P'  -> store = ['P', '', '']
- level = 0 (Top hit!). direction = 1
- level += 1 -> 1

[ Char 2: 'A' ]
- store[1] += 'A'  -> store = ['P', 'A', '']
- level = 1 (Middle). direction stays 1
- level += 1 -> 2

[ Char 3: 'Y' ]
- store[2] += 'Y'  -> store = ['P', 'A', 'Y']
- level = 2 (Bottom hit!). direction = -1
- level += -1 -> 1

[ Char 4: 'P' ]
- store[1] += 'P'  -> store = ['P', 'AP', 'Y']
- level = 1 (Middle). direction stays -1
- level += -1 -> 0

[ Char 5: 'A' ]
- store[0] += 'A'  -> store = ['PA', 'AP', 'Y']
- level = 0 (Top hit!). direction = 1
- level += 1 -> 1

[ Char 6: 'L' ]
- store[1] += 'L'  -> store = ['PA', 'APL', 'Y']
- level = 1. direction = 1
- level += 1 -> 2

[ END ]
- Join the store array: "PA" + "APL" + "Y" = "PAAPLY".

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the length of the string `s`. We iterate through 
  the characters exactly once, and joining an array of strings in Python is also an $O(N)$ 
  operation.
- Space Complexity: $O(N)$. We create a `store` array of size `numRows`, and collectively, 
  these string buckets store all $N$ characters of the original string.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If there's only 1 row (or the string is shorter than the rows),
        # no zigzagging occurs. Return the original string to prevent out-of-bounds errors.
        if numRows == 1 or numRows >= len(s):
            return s
        
        level = 0
        direction = 1
        
        # Create an array of 'numRows' empty strings
        store = [''] * numRows

        for char in s:
            # Append the current character to the string at the current row
            store[level] += char

            # If we hit the top row, switch direction to move downwards
            if level == 0:
                direction = 1
            # If we hit the bottom row, switch direction to move upwards
            elif level == numRows - 1:
                direction = -1
            
            # Move the pointer to the next row based on our current direction
            level += direction
        
        # Concatenate all the rows together into a single string
        return "".join(store)
