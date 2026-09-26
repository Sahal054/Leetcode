"""
543. Diameter of Binary Tree (Post-order DFS)

--- The Core Intuition ---
1. Edges vs. Nodes: The diameter is defined as the number of EDGES between two nodes, 
   not the number of nodes. Conveniently, the number of edges in a path through a node 
   is exactly equal to the height of its left subtree plus the height of its right subtree.
2. The "Split" (Global Maximum): Just like the Maximum Path Sum problem, every single 
   node in the tree has the potential to be the "arch" or "peak" of the longest path. 
   At every node, we calculate `left_height + right_height` and see if it beats our 
   global record (`self.res`).
3. The "Straight Line" (Return Value): When a node reports back to its parent, it 
   cannot offer a forked path. It must choose its longest single branch (either left 
   or right) and add 1 to account for the edge connecting the node to its parent.
4. Scope Management: Here, you used `self.res = 0`. By attaching the variable to the 
   class instance (`self`), you elegantly bypassed the Python scoping issues we discussed 
   earlier, eliminating the need for `res = [0]` or the `nonlocal` keyword.

--- Visual Traversal Walkthrough ---

Example: 
        1
       / \
      2   3
     / \
    4   5

[ INITIAL SETUP ]
- self.res = 0
- dfs(1)

[ DEEP LEFT (Leaves 4 and 5) ]
- dfs(4): 
  - left = 0, right = 0. 
  - Split (left+right) = 0. self.res stays 0. 
  - Returns 1 + max(0,0) = 1.
- dfs(5): 
  - left = 0, right = 0. 
  - Split = 0. self.res stays 0.
  - Returns 1.

[ NODE 2 ]
- left = 1 (from Node 4), right = 1 (from Node 5)
- Split: left + right = 1 + 1 = 2. 
- Update self.res = 2! (Path is 4 -> 2 -> 5, which is 2 edges).
- Returns: 1 + max(1, 1) = 2. (Passes a height of 2 up to Node 1).

[ RIGHT BRANCH (Node 3) ]
- dfs(3):
  - left = 0, right = 0.
  - Returns 1.

[ ROOT NODE 1 ]
- left = 2 (from Node 2), right = 1 (from Node 3)
- Split: left + right = 2 + 1 = 3.
- Update self.res = 3! (Path is 4 -> 2 -> 1 -> 3, which is 3 edges).
- Returns: 1 + max(2, 1) = 3.

[ END ]
- Return self.res, which is 3.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the total number of nodes in the tree. We visit 
  every node exactly once, performing constant time $O(1)$ operations at each.
- Space Complexity: $O(H)$ where $H$ is the height of the tree. This accounts for the 
  recursive call stack. In a balanced tree this is $O(\log N)$, but in a skewed, 
  linked-list-like tree it degrades to $O(N)$.
"""

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use an instance variable to maintain state across all recursive calls
        self.res = 0

        # dfs returns the maximum HEIGHT (depth) of the tree from the current node
        def dfs(node):
            # Base case: an empty node has a height of 0
            if not node:
                return 0
            
            # Post-order traversal: calculate heights of left and right subtrees first
            left = dfs(node.left)
            right = dfs(node.right)
            
            # THE SPLIT: If this node is the peak of the path, the diameter is left + right.
            # Update the global maximum if this is the longest path seen so far.
            self.res = max(self.res, left + right)

            # THE STRAIGHT LINE: Return the height of this subtree to the parent.
            # (1 for the current edge + the longest branch below it)
            return 1 + max(left, right)
        
        # Trigger the DFS traversal
        dfs(root)
        
        return self.res
