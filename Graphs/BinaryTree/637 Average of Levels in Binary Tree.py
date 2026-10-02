"""
637. Average of Levels in Binary Tree (Level Order / BFS)

--- The Core Intuition ---
1. Breadth-First Search (BFS): Whenever a problem asks for data organized strictly 
   "level by level," a Queue-based BFS is the natural choice. We want to process the 
   tree in horizontal slices.
2. The Snapshot Technique: Just like in the "Populating Next Right Pointers" problem, 
   we take a snapshot of the queue's length (`lenq`) at the start of the `while` loop. 
   This locks in exactly how many nodes belong to the current horizontal row, preventing 
   us from accidentally processing the children we are actively adding to the queue.
3. The Math: For each row, we establish a running `sums`. As we pop each node in the row, 
   we add its value to `sums`. Once the inner `for` loop finishes, we have the total sum 
   for that row. We divide it by the number of nodes in that row (`lenq`) to get the average.

--- Visual Traversal Walkthrough ---

Example: 
      3
    /   \
   9     20
        /  \
       15   7

[ INITIAL SETUP ]
- q = [Node(3)]
- res = []

[ LEVEL 1 ]
- lenq = 1
- sums = 0.
- Pop 3. sums = 3. Add children 9, 20. (q = [9, 20])
- Loop finishes. res.append(3 / 1) -> res = [3.0]

[ LEVEL 2 ]
- lenq = 2
- sums = 0.
- Pop 9. sums = 9. No children. (q = [20])
- Pop 20. sums = 29. Add children 15, 7. (q = [15, 7])
- Loop finishes. res.append(29 / 2) -> res = [3.0, 14.5]

[ LEVEL 3 ]
- lenq = 2
- sums = 0.
- Pop 15. sums = 15. No children. (q = [7])
- Pop 7. sums = 22. No children. (q = [])
- Loop finishes. res.append(22 / 2) -> res = [3.0, 14.5, 11.0]

[ END ]
- Queue is empty. Return [3.0, 14.5, 11.0].

--- Complexity & Code Optimization Notes ---
- Time Complexity: Logically $O(N)$ since we visit every node once. However, just like 
  we discussed previously, using `pop(0)` on a standard Python list takes $O(N)$ time 
  per pop, making your specific implementation technically $O(N^2)$. To fix this, swap 
  the list for `collections.deque` and use `popleft()`.
- Space Complexity: $O(N)$ because the queue must hold an entire level of nodes. 
  In a balanced tree, the bottom level holds roughly $N/2$ nodes.
- Minor Redundancy: You declared `avg = 0` but never used it. Additionally, you 
  manually incremented `count`, but `count` will always perfectly equal `lenq` at the 
  end of the loop. You can just divide by `lenq` directly to save a variable!
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        res = []
        q = []
        q.append(root)
        
        while q:
            # Snapshot the exact number of nodes in the current level
            lenq = len(q)
            
            # avg = 0 (Removed: declared but not used)
            sums = 0
            
            # count = 0 (Removed: we can just use 'lenq' for the division)

            # Iterate only through the nodes that belong to this specific level
            for i in range(lenq):
                # Warning: pop(0) is an O(N) operation. Use deque.popleft() for O(1)
                node = q.pop(0)
                
                # Accumulate the sum for the row
                sums += node.val
                
                # Queue up the next level's children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Calculate and store the average for this level
            res.append(sums / lenq)

        return res
