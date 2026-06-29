"""
166. Fraction to Recurring Decimal (Hash Map & Long Division)

The objective is to convert a fraction (given as a numerator and denominator) into 
a string representation of its decimal value. If the fractional part is repeating, 
we must enclose the repeating sequence in parentheses.

Instead of relying on floating-point arithmetic (which loses precision), this 
solution simulates elementary school long division. It uses a Hash Map to detect 
repeating decimal cycles by tracking the remainders we have already seen.

--- The Core Intuition ---
1. Edge Cases & Signs: Handle numerator 0 immediately. Determine the sign by checking 
   if one (and only one) of the numbers is negative. Then, work with absolute values.
2. Long Division (Integer Part): The whole number part is simply `numerator // denominator`. 
   If there's no remainder, we are done.
3. Long Division (Fraction Part): Append a decimal point. To get the next digit, we 
   multiply the remainder by 10 and divide by the denominator again.
4. Cycle Detection: The crucial insight! In division, if you ever see a remainder 
   that you have calculated before, you are stuck in an infinite loop. This means 
   the decimal repeats from the point where you first saw that remainder.
5. Hash Map Tracking: We use `rem_map` to store `{remainder: index_in_res_array}`. 
   When we encounter a duplicate remainder, we use its saved index to insert the 
   opening parenthesis `(`, append the closing parenthesis `)`, and return.

--- Visual Traversal Walkthrough ---

Example: numerator = 1, denominator = 6   (Expected Output: "0.1(6)")

[ INITIAL SETUP ]
- num = 1, den = 6
- Integer part: 1 // 6 = 0
- Remainder: 1 % 6 = 1
- res = ["0", "."]
- rem_map = {}

[ ITERATION 1: rem = 1 ]
- Is 1 in rem_map? No.
- Record position: rem_map[1] = 2 (Because the length of res is 2)
- Multiply rem by 10: rem = 10
- Get next decimal digit: 10 // 6 = 1
- Append to result: res = ["0", ".", "1"]
- Get next remainder: 10 % 6 = 4

[ ITERATION 2: rem = 4 ]
- Is 4 in rem_map? No.
- Record position: rem_map[4] = 3 (Because the length of res is 3)
- Multiply rem by 10: rem = 40
- Get next decimal digit: 40 // 6 = 6
- Append to result: res = ["0", ".", "1", "6"]
- Get next remainder: 40 % 6 = 4

[ ITERATION 3: rem = 4 ]
- Is 4 in rem_map? YES! We found a cycle.
- Where did we first see 4? pos = rem_map[4] -> pos = 3.
- Action: Insert "(" at index 3 in `res`.
  res = ["0", ".", "1", "(", "6"]
- Action: Append ")".
  res = ["0", ".", "1", "(", "6", ")"]
- Return joined result.

Final Return: "0.1(6)"

--- Complexity ---
- Time Complexity: O(d) where d is the absolute value of the denominator. In the worst case, 
  the longest possible length of a repeating cycle in long division is d - 1. 
- Space Complexity: O(d) to store the result string array and the hash map of remainders, 
  which will grow linearly with the length of the fractional part until a cycle is found.
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Edge case: zero numerator
        if numerator == 0:
            return  "0"        
        
        res = []

        # Determine the sign (XOR logic: if signs are different, result is negative)
        if (numerator < 0) != (denominator < 0):
            res.append("-")

        # Work with absolute values to simplify division
        num, den = abs(numerator), abs(denominator)

        # 1. Calculate the integer part
        res.append(str(num // den))

        # 2. Calculate initial remainder
        rem = num % den
        
        # If there is no remainder, it's a clean integer division
        if rem == 0:
            return "".join(res)
        
        # 3. Handle fractional part
        res.append(".")
        rem_map = {}

        # Continue long division as long as there is a remainder
        while rem != 0:
            # If we have seen this remainder before, a repeating cycle is found
            if rem in rem_map:
                pos = rem_map[rem]
                res.insert(pos, "(")
                res.append(")")
                return "".join(res)
            
            # Map the current remainder to its starting index in the result array
            rem_map[rem] = len(res)
            
            # Multiply remainder by 10 (simulate bringing down a zero)
            rem *= 10
            
            # Append the division result
            res.append(str(rem // den))
            
            # Update the remainder for the next iteration
            rem %= den
            
        # Return exact decimal string (no cycles found)
        return "".join(res)
