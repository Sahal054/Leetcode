"""
127. Word Ladder (Graph & Breadth-First Search)

The objective is to find the length of the shortest transformation sequence from a 
`beginWord` to an `endWord`. In this sequence, every adjacent pair of words must differ 
by exactly one single character, and every intermediate word must exist in the `wordList`.

This solution uses Breadth-First Search (BFS) to guarantee the shortest path. The brilliance 
of this specific approach is how it optimizes finding neighboring words using a "pattern" 
dictionary, rather than doing an expensive comparison of every word against every other word.

--- The Core Intuition ---
1. The Bottleneck: Normally, to find words that differ by one letter, you might compare 
   word A to word B letter by letter. If you have a massive dictionary, doing this for 
   every word combination results in a Time Limit Exceeded (TLE) error.
2. The Pattern Optimization: Instead of comparing words to each other, we group them by 
   patterns. If a word is "hot", we create three patterns: "*ot", "h*t", and "ho*". We 
   map these patterns to the word in a dictionary. 
3. Building the Graph: Any words that share a pattern differ by exactly one letter! For 
   example, "hot" and "dot" both map to the pattern "*ot". This allows us to instantly 
   find all valid neighbors for any given word.
4. BFS Traversal: We start with a queue containing `beginWord` and a `res` (result) counter 
   at 1. We process the queue level by level. For each word, we generate its patterns, look 
   up its neighbors in our pattern dictionary, and add unvisited neighbors to the queue.
5. The Exit: Because we are using BFS, the very first time we pop `endWord` from our queue, 
   we are guaranteed it is the shortest path, and we return our `res` counter.

--- Visual Traversal Walkthrough ---

Example: beginWord = "hit", endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

[ PRE-PROCESSING ]
Add "hit" to wordList. 
Build `nei` dictionary:
"*ot" -> ["hot", "dot", "lot"]
"h*t" -> ["hot", "hit"]
"ho*" -> ["hot"]
"c*g" -> ["cog"]
...and so on.

[ INITIAL SETUP ]
queue = ["hit"], visit = {"hit"}, res = 1

[ BFS LEVEL 1 ]
- queue size = 1. Pop "hit".
- Is "hit" == "cog"? No.
- Patterns for "hit": "*it", "h*t", "hi*"
- Neighbors found in "h*t": ["hot"] (we skip "hit" because it's in `visit`)
- Add "hot" to queue and `visit`.
- Queue is now empty for this level. Increment res to 2.
Current Queue: ["hot"]

[ BFS LEVEL 2 ]
- queue size = 1. Pop "hot".
- Patterns for "hot": "*ot", "h*t", "ho*"
- Neighbors found in "*ot": ["dot", "lot"] 
- Add "dot", "lot" to queue and `visit`.
- Increment res to 3.
Current Queue: ["dot", "lot"]

[ BFS LEVEL 3 ]
- queue size = 2. 
- Pop "dot" -> adds "dog" to queue.
- Pop "lot" -> adds "log" to queue.
- Increment res to 4.
Current Queue: ["dog", "log"]

[ BFS LEVEL 4 ]
- queue size = 2.
- Pop "dog" -> Patterns include "*og", "d*g", "do*".
- "*og" neighbors: ["log", "cog"].
- Add "cog" to queue and `visit`. (Skip "log", already visited).
- Pop "log" -> no new unvisited neighbors.
- Increment res to 5.
Current Queue: ["cog"]

[ BFS LEVEL 5 ]
- Pop "cog". 
- "cog" == endWord! Return res (5).

--- Complexity ---
- Time Complexity: $O(N \cdot M^2)$ where $N$ is the total number of words and $M$ is the 
  length of each word. We iterate through $N$ words, and for each word, we take $M$ iterations 
  to create patterns. Furthermore, string slicing in Python (`word[:j] + "*" + word[j+1:]`) 
  takes $O(M)$ time, resulting in $M \cdot M = M^2$ operations per word.
- Space Complexity: $O(N \cdot M^2)$ for the `nei` dictionary. We store $N$ words, and each 
  word is associated with $M$ patterns. The queue and visit set also take up to $O(N)$ space, 
  but the adjacency list dominates the memory footprint.
"""

from typing import List
import collections
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the target word isn't even in the dictionary, a path is impossible.
        if endWord not in wordList:
            return 0
        
        # Dictionary to map patterns to a list of words that match that pattern
        # e.g., "h*t" : ["hot", "hit"]
        nei = collections.defaultdict(list)
        
        # We must add beginWord to the list so we can map its patterns too
        wordList.append(beginWord)

        # Pre-processing: Build the adjacency list based on wildcard patterns
        for word in wordList:
            for j in range(len(word)):
                # Create a pattern by replacing the j-th character with an asterisk
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
            
        # Initialize the BFS queue and the visited set to prevent cycles
        queue = deque()
        queue.append(beginWord)
        visit = set([beginWord])
        
        # res tracks the number of words in the transformation sequence (levels of BFS)
        res = 1
        
        while queue:
            # Iterate through exactly the number of elements currently in the queue
            # This ensures we process the graph level by level.
            for i in range(len(queue)):
                word = queue.popleft()

                # If we've reached our target, return the current sequence length
                if word == endWord:
                    return res
                
                # Generate patterns for the popped word to find its neighbors
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    # Iterate through all words that share this pattern
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            queue.append(neiword)
            
            # After finishing a full level of neighbors, increment our sequence length
            res += 1
            
        # If the queue empties and we haven't returned, no path exists
        return 0
