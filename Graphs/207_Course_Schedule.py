"""
207. Course Schedule (Graph & Depth-First Search / Cycle Detection)

The objective is to determine if you can finish all courses given a list of prerequisite 
pairs. This problem translates directly to detecting if there is a cycle in a directed 
graph. If a cycle exists (e.g., A requires B, B requires C, and C requires A), it is 
impossible to finish the courses.

This solution models the courses as nodes and prerequisites as directed edges in an 
adjacency list. It uses Depth-First Search (DFS) to traverse the prerequisite chain for 
each course. 

--- The Core Intuition ---
1. Graph Construction: We build an adjacency list `adj` where each course points to a 
   list of its immediate prerequisites.
2. The "Active Path" Tracker: The `visit` set tracks courses that are currently in our 
   active DFS path. If we ever try to visit a course that is already in `visit`, it 
   means we've looped back on ourselves -> A CYCLE EXISTS!
3. Base Cases:
   - If `crs` is in `visit`, return False (Cycle detected).
   - If `adj[crs]` is empty `[]`, return True (No prereqs, or we already cleared them).
4. Backtracking & Optimization: After successfully verifying all prerequisites for a 
   course, we remove it from the `visit` set so other branches can safely visit it. 
   CRUCIALLY, we set `adj[crs] = []`. This acts as a memoization step—if another course 
   requires this one later, we instantly know it's valid without re-running the DFS.
5. Global Check: The graph might consist of disconnected components (e.g., courses 0 
   and 1 are related, but course 2 is independent). We must run a loop to start DFS 
   from every single course from `0` to `numCourses - 1`.

--- Visual Traversal Walkthrough ---

Example Graph (A Cycle): numCourses = 3, prerequisites = [[0, 1], [1, 2], [2, 0]]
Meaning: 0 requires 1. 1 requires 2. 2 requires 0.

[ INITIAL SETUP ]
adj = {
  0: [1],
  1: [2],
  2: [0]
}
visit = {}

[ OUTER LOOP: Start with crs 0 ]
-> Run DFS(0):
   - Add 0 to visit. visit = {0}
   - Check prereqs of 0: finds 1.
   
   -> Run DFS(1):
      - Add 1 to visit. visit = {0, 1}
      - Check prereqs of 1: finds 2.
      
      -> Run DFS(2):
         - Add 2 to visit. visit = {0, 1, 2}
         - Check prereqs of 2: finds 0.
         
         -> Run DFS(0):
            - Is 0 in visit? YES! It's in our active path {0, 1, 2}.
            - CYCLE DETECTED. Return False.
            
      <- DFS(2) receives False from DFS(0). Returns False.
   <- DFS(1) receives False from DFS(2). Returns False.
<- DFS(0) receives False from DFS(1). Returns False.

[ FINAL RETURN ]
Since DFS(0) returned False, the outer loop immediately returns False. You cannot 
finish these courses.

*What if it wasn't a cycle?* If 2 didn't require 0, DFS(2) would succeed. It would remove 2 from `visit` and set 
`adj[2] = []`. Then DFS(1) would succeed, set `adj[1] = []`, and so on.

--- Complexity ---
- Time Complexity: O(V + E) where V is the number of courses (vertices) and E is the 
  number of prerequisites (edges). Because we set `adj[crs] = []` upon success, we never 
  process a node or its edges more than once.
- Space Complexity: O(V + E) to store the adjacency list. The `visit` set and the DFS 
  recursion call stack will take up to O(V) space in the worst case (a single straight line 
  of prerequisites).
"""

import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency list mapping each course to its prerequisites
        adj = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # Set to keep track of courses along the current DFS path
        visit = set()
        
        def dfs(crs):
            # If the course is already in the active path, we found a cycle
            if crs in visit:
                return False
            
            # If the course has no prerequisites, it can definitely be completed
            if adj[crs] == []:
                return True
            
            # Mark the course as currently being visited
            visit.add(crs)
            
            # Recursively check all prerequisites for this course
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
                    
            # Backtrack: remove from active path so other branches can visit it
            visit.remove(crs)
            
            # Optimization (Memoization): mark this course as completely verified.
            # If we reach it from another path later, we instantly return True.
            adj[crs] = []
            
            return True
        
        # We must check every course because the graph might have disconnected components
        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        # If no cycles were found in any component, it's possible to finish all courses
        return True
