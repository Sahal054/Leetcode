"""
101. Symmetric Tree (Recursive Depth-First Search)

--- The Core Intuition ---
1. The Mirror Image Concept: A tree is symmetric if the left subtree is a mirror reflection 
   of the right subtree. This means the left child's value must equal the right child's value.
2. Outer vs. Inner Children: The trickiest part is how to continue the check downward. 
   To be a mirror, the "outer" children must match, and the "inner" children must match.
   - The LEFT child's LEFT subtree must match the RIGHT child's RIGHT subtree (Outer).
   - The LEFT child's RIGHT subtree must match the RIGHT child's LEFT subtree (Inner).
3. The Helper Function: Since the main function only takes one `root`, we need a helper 
   function `dfs(left, right)` that allows us to pass down and compare two nodes 
   simultaneously, exactly like we did in "Same Tree".

--- Visual Traversal Walkthrough ---

Example: 
         1
       /   \
      2     2
     / \   / \
    3   4 4   3

[ INITIAL CALL ]
- Main function calls dfs(root.left, root.right) -> dfs(2, 2)

[ COMPARING THE 2s ]
- left = 2, right = 2. Values match!
- Now, we branch out and make two recursive calls:
  1. Outer children: dfs(left.left, right.right) -> dfs(3, 3)
  2. Inner children: dfs(left.right, right.left) -> dfs(4, 4)

[ OUTER CHILDREN CALL (3s) ]
- left = 3, right = 3. Values match!
- Outer: dfs(None, None) -> True
- Inner: dfs(None, None) -> True
- Branch returns True.

[ INNER CHILDREN CALL (4s) ]
- left = 4, right = 4. Values match!
- Outer: dfs(None, None) -> True
- Inner: dfs(None, None) -> True
- Branch returns True.

[ END ]
- Both the outer branch and inner branch returned True. 
- The root 2s return True. The tree is symmetric.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the total number of nodes in the tree. In the 
  worst case, we have to visit every single node to verify perfect symmetry.
- Space Complexity: $O(H)$ where $H$ is the height of the tree, representing the maximum 
  depth of the recursive call stack. In a perfectly balanced symmetric tree, this is $O(\log N)$.
"""

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Helper function to compare two nodes as mirrors of each other
        def dfs(left, right):
            # Base case 1: Both nodes are null. They are perfect mirrors.
            if not left and not right:
                return True
            
            # Base case 2: Only one node is null. The symmetry is broken.
            if not left or not right:
                return False 
            
            # Recursive step: 
            # 1. The current values must match.
            # 2. The OUTER children must match (left's left with right's right).
            # 3. The INNER children must match (left's right with right's left).
            return (
                (left.val == right.val) and 
                dfs(left.left, right.right) and
                dfs(left.right, right.left)
            )

        # Start the recursion by comparing the root's left and right subtrees
        return dfs(root.left, root.right)
