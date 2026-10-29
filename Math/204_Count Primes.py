"""
204. Count Primes (Sieve of Eratosthenes)

--- The Core Intuition ---
1. The Elimination Strategy (The Sieve): Instead of checking if every individual number 
   is prime (which is incredibly slow), we assume EVERY number is prime initially. Then, 
   we iterate through the numbers and systematically "cross out" all multiples of known primes.
2. The Inner Loop Optimization (i * i): You correctly noted changing `2 * i` to `i * i`. 
   Why is this brilliant? If you are crossing out multiples of 5, you don't need to cross 
   out 10 (already crossed out by 2), 15 (crossed out by 3), or 20 (crossed out by 2). 
   The very first multiple of 5 that hasn't been crossed out yet is ALWAYS 5 * 5 = 25.
3. The Outer Loop Bound (Square Root): Approach 1 stops checking at `int(n**0.5)`. 
   Why? Because if a number `k` is composite, it MUST have at least one prime factor 
   less than or equal to `sqrt(k)`. Therefore, all composite numbers up to `n` will 
   already be crossed out by the time we finish processing primes up to `sqrt(n)`. 
   Approach 2 runs all the way to `n`, which still works but does unnecessary empty iterations.

--- Visual Traversal Walkthrough ---

Example: n = 10 (We need primes strictly less than 10: 2, 3, 5, 7. Total = 4)
Initial pnums: [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]  (Indices 0 to 9. 0 and 1 are not prime)

[ OUTER LOOP: i = 2 ]
- pnums[2] is 1 (Prime).
- Inner loop starts at 2*2 = 4, steps by 2: (4, 6, 8)
- Cross them out: pnums[4]=0, pnums[6]=0, pnums[8]=0.
- State: [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]

[ OUTER LOOP: i = 3 ]
- pnums[3] is 1 (Prime).
- Inner loop starts at 3*3 = 9, steps by 3: (9)
- Cross it out: pnums[9]=0.
- State: [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]

[ END OF ALGORITHM ]
- If using Approach 1, sqrt(10) is ~3.16, so the loop stops here! 
- Remaining 1s in pnums: indices 2, 3, 5, 7.
- Total count = 4.

--- Complexity ---
- Time Complexity: $O(N \log \log N)$. This is a famous mathematical bound for the 
  Sieve of Eratosthenes. The harmonic series of primes grows extremely slowly, making 
  this highly efficient and nearly linear in practice.
- Space Complexity: $O(N)$ to store the `pnums` boolean array representing numbers up to `n`.
"""

class Solution:
    # --- APPROACH 1: Fully Optimized Sieve (Outer loop stops at sqrt(n)) ---
    def countPrimesOptimized(self, n: int) -> int:
        if n <= 2:
            return 0 

        # Initialize array where 1 means prime, 0 means composite
        pnums = [1] * n
        pnums[0] = pnums[1] = 0

        count = 0

        # OPTIMIZATION 1: We only need to process up to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if pnums[i] == 1:
                
                # OPTIMIZATION 2: Start crossing out multiples at i * i
                for j in range(i * i, n, i):
                    pnums[j] = 0
                
        # Count the remaining 1s (Python trick: you can also just do `return sum(pnums)`)
        for i in pnums:
            if i == 1:
                count += 1
        
        return count


    # --- APPROACH 2: Standard Sieve (Outer loop runs to n) ---
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0 

        pnums = [1] * n
        pnums[0] = pnums[1] = 0
        count = 0

        # Runs all the way to n. Safe, but executes empty checks for numbers > sqrt(n)
        for i in range(2, n):
            if pnums[i] == 1:
                # Still utilizes the great i * i optimization!
                for j in range(i * i, n, i):
                    pnums[j] = 0
                
        for i in pnums:
            if i == 1:
                count += 1
        
        return count
