"""
210. Course Schedule II (Topological Sort & Depth-First Search)

The objective is to find a valid order in which to take a given number of courses 
based on their prerequisites. If it's impossible to finish all courses (due to a 
cycle), we must return an empty array. 

This solution builds directly on "Course Schedule I". However, instead of just 
returning True/False, it uses Topological Sorting. By appending courses to an output 
list only AFTER all their prerequisites have been fully resolved, it naturally builds 
a valid chronological timeline from the ground up.

--- The Core Intuition ---
1. Graph Construction: We build an adjacency list `adj` where each course points to 
   a list of its immediate prerequisites.
2. The Three States of a Course: 
   To manage the traversal, a course can be in one of three states:
   - Unvisited: Not in any set. We haven't looked at it yet.
   - Visiting (`cycle` set): Currently in our active DFS path. If we hit this again, 
     we found a cycle (a paradox), and we abort.
   - Visited (`visit` set): Fully processed. All of its prerequisites have been 
     checked and added to the output. If we hit this again, we can instantly return True 
     because we already know it's safe.
3. Post-Order Append: The absolute key to Topological Sort. We only add a course to 
   the `output` array at the VERY END of its DFS function. This guarantees that before 
   Course A is added, all prerequisites of Course A have already been added.
4. Global Loop: Just like Course Schedule I, we loop through every single course 
   (`0` to `numCourses - 1`) to ensure we don't miss disconnected graph components.

--- Visual Traversal Walkthrough ---

Example Graph: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Meaning: 0 is required for 1 and 2. Both 1 and 2 are required for 3.

[ INITIAL SETUP ]
adj = { 1: [0], 2: [0], 3: [1, 2], 0: [] }
cycle = {}   |   visit = {}   |   output = []

[ OUTER LOOP: Start with crs 0 ]
-> Run DFS(0):
   - Add 0 to cycle.
   - Prereqs of 0? None.
   - Remove 0 from cycle, add 0 to visit.
   - Append 0 to output! 
     State: visit = {0} | output = [0]

[ OUTER LOOP: Move to crs 1 ]
-> Run DFS(1):
   - Add 1 to cycle.
   - Prereqs of 1? Finds 0.
   -> Run DFS(0):
      - 0 is already in `visit`! Returns True instantly (O(1) time).
   - Remove 1 from cycle, add 1 to visit.
   - Append 1 to output!
     State: visit = {0, 1} | output = [0, 1]

[ OUTER LOOP: Move to crs 2 ]
-> Run DFS(2):
   - Add 2 to cycle.
   - Prereqs of 2? Finds 0.
   -> Run DFS(0): 
      - 0 is in `visit`! Returns True.
   - Remove 2 from cycle, add 2 to visit.
   - Append 2 to output!
     State: visit = {0, 1, 2} | output = [0, 1, 2]

[ OUTER LOOP: Move to crs 3 ]
-> Run DFS(3):
   - Add 3 to cycle.
   - Prereqs of 3? Finds 1 and 2.
   -> Run DFS(1): in `visit`, returns True.
   -> Run DFS(2): in `visit`, returns True.
   - Remove 3 from cycle, add 3 to visit.
   - Append 3 to output!
     State: visit = {0, 1, 2, 3} | output = [0, 1, 2, 3]

Final Return: [0, 1, 2, 3]

--- Complexity ---
- Time Complexity: O(V + E) where V is the number of courses (vertices) and E is the 
  number of prerequisites (edges). Because of the `visit` set, we never process a node 
  or its edges more than once.
- Space Complexity: O(V + E) to store the adjacency list. The `cycle` set, `visit` set, 
  `output` array, and the DFS recursion call stack will take up to O(V) space.
"""

from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Adjacency list mapping each course to its prerequisites
        adj = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # 'cycle' tracks nodes in the current DFS path (to detect cycles)
        cycle = set() 
        # 'visit' tracks nodes that have been fully processed and added to output
        visit = set()
        # Array to store the final topological order
        output = []
        
        def dfs(crs):
            # If the course is in our active path, a cycle exists. Invalid schedule.
            if crs in cycle:
                return False
            # If the course is fully processed, we don't need to do it again.
            if crs in visit:
                return True
            
            # Add to active path
            cycle.add(crs)

            # Recursively process all prerequisites
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
                
            # Backtrack: remove from active path
            cycle.remove(crs)
            
            # Mark as completely processed
            visit.add(crs)
            
            # POST-ORDER APPEND: Because all prerequisites have finished running 
            # and returned True, it is now safe to add this course to our timeline.
            output.append(crs)

            return True
        
        # Iterate through every course to ensure we cover disconnected components
        for n in range(numCourses):
            # If any DFS detects a cycle, it returns False. Return empty array.
            if not dfs(n):
                return []
        
        return output
