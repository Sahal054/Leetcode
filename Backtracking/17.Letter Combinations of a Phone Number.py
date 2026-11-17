"""
17. Letter Combinations of a Phone Number (Backtracking / Decision Tree)

--- The Core Intuition ---
1. Dynamic Cartesian Product: If `digits` always had length 2 (like `"23"`), you could 
   just write two nested `for` loops. Because `digits` can be anywhere from 0 to 4 
   characters long, we use Backtracking to dynamically generate `N` nested loops—one 
   level of recursion for each digit in the input string.
2. Index-Driven State (`i`): Unlike Combinations (where we needed a `start` pointer to 
   avoid duplicate sets) or Permutations (where we needed a visited check), here each 
   position `i` in the output string comes from its own completely separate pool of 
   letters (`digi[digits[i]]`). Advancing `i + 1` naturally moves us to the next keypad digit.
3. The Edge Case (`digits == ""`): If the input string is empty, `len(comb) == len(digits)` 
   (`0 == 0`) would trigger immediately on the first call and return `[""]` instead of `[]`. 
   Adding an `if not digits: return []` guard at the top cleanly handles empty inputs.
4. Mutable List + Join (`"".join(comb)`): Building the path in a mutable list `comb` 
   and joining it into a string only at the base case avoids creating dozens of intermediate 
   string copies during recursion, while still allowing $O(1)$ `append()` and `pop()` cleanup.

--- Visual Traversal Walkthrough ---

Example: digits = "23"
Map: '2' -> "abc", '3' -> "def"
Initial state: res = [], comb = []

[ LEVEL 0: DIGIT '2' (i = 0) ]
- Loop c in "abc":
  - c = 'a':
    - comb.append('a') -> comb = ['a']
    - Call backtrack(i=1, comb=['a'])

[ LEVEL 1: DIGIT '3' (i = 1) ]
- Loop c in "def":
  - c = 'd':
    - comb = ['a', 'd'] -> BASE CASE HIT (len == 2)!
    - res.append("ad") -> res = ["ad"]
    - comb.pop() -> comb = ['a']
  - c = 'e':
    - comb = ['a', 'e'] -> BASE CASE HIT!
    - res.append("ae") -> res = ["ad", "ae"]
    - comb.pop() -> comb = ['a']
  - c = 'f':
    - comb = ['a', 'f'] -> BASE CASE HIT!
    - res.append("af") -> res = ["ad", "ae", "af"]
    - comb.pop() -> comb = ['a']
- Level 1 loop finishes for 'a'.

[ THE UNDO AT LEVEL 0 ]
- Back in Level 0: comb.pop() -> comb = []
- Loop moves to c = 'b':
  - Appends 'b', explores "bd", "be", "bf", pops back to []...
- Loop moves to c = 'c':
  - Appends 'c', explores "cd", "ce", "cf", pops back to []...

[ RESOLUTION ]
- Tree fully traversed.
- Return res: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

--- Complexity ---
- Time Complexity: $O(N \times 4^N)$ where $N$ is the length of `digits`. In the worst case 
  (digits consisting of `'7'` or `'9'`, which map to 4 letters), the decision tree branches 
  4 ways at every level, producing $4^N$ combinations. Each combination takes $O(N)$ time 
  to join into a string at the leaf node.
- Space Complexity: $O(N)$ auxiliary space for the recursive call stack depth and the `comb` 
  buffer list (excluding the $O(N \times 4^N)$ memory required to store the output list `res`).
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Guard clause: An empty input should return an empty list, not [""]
        if not digits:
            return []

        digi = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []

        def backtrack(i, comb):
            # Base Case: We have picked one letter for every digit in the input
            if len(comb) == len(digits):
                # Join the character buffer into an immutable string
                res.append("".join(comb))
                return
            
            # Grab the keypad letters corresponding to the current digit index 'i'
            digit = digits[i]

            for c in digi[digit]:
                # 1. MAKE A CHOICE
                comb.append(c)
                
                # 2. EXPLORE THAT CHOICE (advance to the next digit index i + 1)
                backtrack(i + 1, comb)
                
                # 3. UNDO THE CHOICE (Backtrack)
                comb.pop()
        
        # Start at index 0 with an empty character buffer
        backtrack(0, [])
        return res
