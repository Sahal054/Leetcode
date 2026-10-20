"""
139. Word Break (Top-Down Dynamic Programming / Memoization)

--- The Core Intuition ---
1. The Decision Tree: At the beginning of the string (index 0), we don't know which 
   word to extract. So, we look through our `wordDict` and ask: "Does the string start 
   with this word right here?"[cite: 1]
2. The Recursive Leap: If a word matches the prefix perfectly, we take a leap forward. 
   If the word is "leet" (length 4), we jump to index 4 and recursively ask the exact 
   same question: "Can the rest of the string starting from index 4 be broken down?"
3. The Overlapping Subproblems: Imagine a dictionary like `["a", "aa", "b"]` and a 
   string `"aaaaab"`. You could arrive at index 2 by picking `"a"` twice, or by picking 
   `"aa"` once. Without a cache, naive recursion recalculates the exact same suffix 
   from index 2 repeatedly. 
4. The Memoization: We use a `memo` dictionary to cache indices. `memo[i]` will store 
   a boolean indicating whether the substring `s[i:]` can be successfully broken down. 
   If we hit a dead end, we cache `memo[i] = False` and instantly short-circuit any 
   future paths that land on index `i`.

--- Visual Traversal Walkthrough ---

Example: s = "leetcode", wordDict = ["leet", "code"][cite: 1]

[ INITIAL CALL ]
- dfs(0): Standing at the start of "leetcode".
- Try "leet": `s.startswith("leet", 0)` is True! 
- Leap forward by len("leet") (4). Call dfs(4).

[ RECURSIVE CALL 1 ]
- dfs(4): Standing at "code".
- Try "leet": `s.startswith("leet", 4)` is False.
- Try "code": `s.startswith("code", 4)` is True!
- Leap forward by len("code") (4). Call dfs(8).

[ BASE CASE ]
- dfs(8): i == len(s) (8 == 8). We successfully consumed the whole string!
- Return True.

[ RESOLUTION ]
- dfs(4) receives True. CACHE: memo[4] = True. Returns True.
- dfs(0) receives True. CACHE: memo[0] = True. Returns True.

--- Complexity ---
- Time Complexity: $O(N \times M \times L)$ where $N$ is the length of string `s`, 
  $M$ is the number of words in `wordDict`, and $L$ is the maximum length of a word 
  in the dictionary (due to string comparison). Because of our `memo` cache, we only 
  process each of the $N$ starting indices once.
- Space Complexity: $O(N)$ for the recursive call stack depth and the `memo` dictionary 
  storing up to $N$ indices.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Cache to store whether the substring starting at index 'i' can be segmented
        memo = {}

        def dfs(i):
            # Base Case: If we exactly reached the end of the string, it's a valid breakdown
            if i == len(s):
                return True
            
            # Cache Check: If we already know the answer for this index, return it instantly
            if i in memo:
                return memo[i]
            
            # Try to match every single word in the dictionary at the current index
            for word in wordDict:
                
                # Check if the remaining string starts with 'word' exactly at index 'i'
                if s.startswith(word, i):
                    
                    # Leap forward by the length of the matched word
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
                        
            # If no dictionary word can be matched from this index to form a valid sentence,
            # mark this index as a dead end.
            memo[i] = False
            return False
            
        return dfs(0)
