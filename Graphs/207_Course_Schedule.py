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
  0: 
