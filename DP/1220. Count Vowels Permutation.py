"""
1220. Count Vowels Permutation (Bottom-Up Dynamic Programming / O(1) Space State Machine)

--- The Core Intuition ---
1. Flipping the Rules (Incoming vs. Outgoing Transitions): The problem gives us rules 
   for what can *follow* each vowel (e.g., 'a' -> 'e'). To build strings forward by 
   appending one character at a time, we invert those rules to ask: "Which previous 
   vowels can transition *into* my current vowel?"
   - To end in 'a': Must come from 'e', 'i', or 'u'  ->  new_a = e + i + u
   - To end in 'e': Must come from 'a' or 'i'         ->  new_e = a + i
   - To end in 'i': Must come from 'e' or 'o'         ->  new_i = e + o
   - To end in 'o': Must come from 'i'                ->  new_o = i
   - To end in 'u': Must come from 'o' or 'i'         ->  new_u = o + i
2. State Compression (O(1) Space): Normally, a 2D DP table `dp[length][vowel]` would 
   store counts for every string length from 1 to `n`. However, calculating strings of 
   length `L` ONLY depends on the counts from length `L - 1`. This allows us to throw 
   away the entire table and track just 5 integer variables (`a, e, i, o, u`).
3. The Base Case (Length = 1): For a string of length 1, each of the 5 vowels forms 
   exactly 1 valid single-character string (`"a"`, `"e"`, `"i"`, `"o"`, `"u"`), so we 
   initialize all five counters to `1` and run the loop `n - 1` times.
4. Simultaneous Tuple Unpacking: Writing `a, e, i, o, u = ...` on a single line in Python 
   evaluates the entire right-hand side *before* updating any variable on the left. 
   This acts like a built-in `nextDp` snapshot, preventing newly updated counts from 
   corrupting calculations within the same iteration.

--- Visual Traversal Walkthrough ---

Example: n = 3

[ INITIAL SETUP: LENGTH 1 ]
- a = 1, e = 1, i = 1, o = 1, u = 1
- Total valid strings of length 1 = 5 ("a", "e", "i", "o", "u")

[ ITERATION 1: BUILDING LENGTH 2 ]
- new_a = e + i + u = 1 + 1 + 1 = 3  ("ea", "ia", "ua")
- new_e = a + i     = 1 + 1     = 2  ("ae", "ie")
- new_i = e + o     = 1 + 1     = 2  ("ei", "oi")
- new_o = i         = 1         = 1  ("io")
- new_u = o + i     = 1 + 1     = 2  ("ou", "iu")
- State: a=3, e=2, i=2, o=1, u=2  (Total = 10)

[ ITERATION 2: BUILDING LENGTH 3 ]
- new_a = e + i + u = 2 + 2 + 2 = 6
- new_e = a + i     = 3 + 2     = 5
- new_i = e + o     = 2 + 1     = 3
- new_o = i         = 2         = 2
- new_u = o + i     = 1 + 2     = 3
- State: a=6, e=5, i=3, o=2, u=3

[ RESOLUTION ]
- Sum all states: (6 + 5 + 3 + 2 + 3) % (10**9 + 7) = 19.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the target string length. The loop runs $N - 1$ 
  times, performing a constant number of additions per step. (Note: In Python, arbitrary-precision 
  integers handle huge intermediate sums automatically, though applying `% MOD` inside 
  the loop keeps integer sizes small and prevents slow big-int arithmetic for large $N$).
- Space Complexity: $O(1)$ auxiliary space. We use only 5 variables regardless of how 
  large $N$ grows.
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case (n = 1): Each variable represents the number of valid strings
        # of the current length that end with that specific vowel.
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        # Transition from length 1 up to length n (n - 1 steps)
        for _ in range(n - 1):
            # Simultaneous unpacking updates all 5 states from the previous step at once
            a, e, i, o, u = (
                (e + i + u) % MOD,  # Vowels that can precede 'a'
                (a + i) % MOD,      # Vowels that can precede 'e'
                (e + o) % MOD,      # Vowels that can precede 'i'
                i % MOD,            # Vowels that can precede 'o'
                (o + i) % MOD       # Vowels that can precede 'u'
            )
        
        # Total valid strings of length n is the sum of strings ending in any vowel
        return (a + e + i + o + u) % MOD
