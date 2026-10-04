"""
103. Binary Tree Zigzag Level Order Traversal (BFS with Level Reversal)

--- The Core Intuition ---
1. Standard BFS Baseline: We use a standard Queue-based Level Order Traversal exactly 
   like we did for "Average of Levels" and "Right Side View". We always append the 
   left child first, then the right child.
2. The Zigzag Flag: We introduce a boolean flag (`left_to_right`) that starts as `True`. 
   At the end of processing every level, we flip this flag to its opposite state.
3. The Reversal Trick: If `left_to_right` is False, it means we are on a zigzag row 
   (like Level 1 or Level 3). We simply take the perfectly ordered `level` array we 
   just built and reverse it (`level.reverse()`) before adding it to our final `res` list.

--- Visual Traversal Walkthrough ---

Example: 
      3
    /   \
   9     20
        /  \
       15   7

[ INITIAL SETUP ]
- q = deque([3])
- left_to_right = True

[ LEVEL 0 ]
- lenq = 1. level = [].
- Pop 3. level = [3]. Add 9, 20. (q = [9, 20])
- left_to_right is True? Yes. Keep level as [3].
- res = [[3]]
- Flip flag: left_to_right = False

[ LEVEL 1 ]
- lenq = 2. level = [].
- Pop 9. level = [9]. No children. (q = [20])
- Pop 20. level = [9, 20]. Add 15, 7. (q = [15, 7])
- left_to_right is True? No. REVERSE level -> [20, 9].
- res = [[3], [20, 9]]
- Flip flag: left_to_right = True

[ LEVEL 2 ]
- lenq = 2. level = [].
- Pop 15. level = [15]. No children. (q = [7])
- Pop 7. level = [15, 7]. No children. (q = [])
- left_to_right is True? Yes. Keep level as [15, 7].
- res = [[3], [20, 9], [15, 7]]
- Flip flag: left_to_right = False

[ END ]
- Return res: [[3], [20, 9], [15, 7]]

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes. We visit each node once 
  to add it to a level list. Reversing a level of size $K$ takes $O(K)$ time, and 
  since all levels combined equal $N$ nodes, the total reversal time across the whole 
  algorithm is strictly $O(N)$.
- Space Complexity: $O(N)$ for the queue and the level arrays.
"""

import collections
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        # Use deque for O(1) pops from the front
        q = collections.deque([root])
        
        # Track the direction of the current level
        left_to_right = True

        while q:
            lenq = len(q)
            level = []

            for _ in range(lenq):
                node = q.popleft()
                level.append(node.val)

                # ALWAYS push left then right, regardless of zigzag direction
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # If we are on a right-to-left level, simply reverse the collected values
            if not left_to_right:
                level.reverse()
                
            res.append(level)
            
            # Toggle the direction for the next level
            left_to_right = not left_to_right
        
        return res
