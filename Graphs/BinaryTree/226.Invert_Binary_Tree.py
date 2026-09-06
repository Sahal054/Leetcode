"""
226. Invert Binary Tree (Recursive Depth-First Search)

--- The Core Intuition ---
1. The Mirror Image: Inverting a binary tree means creating a perfect mirror image of it. 
   Every left child becomes a right child, and every right child becomes a left child.
2. The Top-Down Swap: We can approach this top-down (Pre-order traversal). When we visit 
   a node, we simply swap its left and right pointers. Python makes this incredibly clean 
   with simultaneous assignment (tuple unpacking), preventing the need for a `temp` variable.
3. The Recursive Delegation: After a node swaps its immediate children, its job is mostly done. 
   However, the subtrees underneath those children are still in their original order! We must 
   recursively call the function on both the new left child and the new right child so they 
   can invert their own subtrees.
4. The Base Case: If we hit a `None` (an empty spot where a child should be), there is 
   nothing to invert, so we just return `None`.

--- Visual Traversal Walkthrough ---

Example: 
     Original                 Inverted
        4                        4
      /   \        --->        /   \
     2     7                  7     2
    / \   / \                / \   / \
   1   3 6   9              9   6 3   1

[ INITIAL CALL: Root = 4 ]
- root is 4. Not null.
- Swap children: root.left becomes 7, root.right becomes 2.
- Tree so far: 
        4
      /   \
     7     2
- Call invertTree(root.left), which is now the node 7!

[ LEFT CHILD CALL: Node = 7 ]
- root is 7. Not null.
- Swap children: root.left becomes 9, root.right becomes 6.
- Call invertTree(root.left) -> Node 9 -> Returns None (leaf).
- Call invertTree(root.right) -> Node 6 -> Returns None (leaf).
- Return node 7.

[ RIGHT CHILD CALL: Node = 2 ]
- (Backing up to root 4, it now calls invertTree(root.right), which is 2)
- root is 2. Not null.
- Swap children: root.left becomes 3, root.right becomes 1.
- Call invertTree(root.left) -> Node 3 -> Returns None.
- Call invertTree(root.right) -> Node 1 -> Returns None.
- Return node 2.

[ END ]
- Root 4 finishes its calls and returns itself. The entire tree is mirrored.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the total number of nodes in the tree. We must 
  visit and swap the children of every single node exactly once.
- Space Complexity: $O(H)$ where $H$ is the height of the tree. This accounts for the 
  recursive call stack. In a perfectly balanced tree, this is $O(\log N)$. In the worst-case 
  scenario (a straight-line tree like a linked list), it degrades to $O(N)$.
"""

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the current node is empty, just return None
        if not root:
            return None
        
        # Swap the left and right children using Python's simultaneous assignment
        root.left, root.right = root.right, root.left

        # Recursively invert the left subtree (which used to be the right subtree)
        self.invertTree(root.left)
        
        # Recursively invert the right subtree (which used to be the left subtree)
        self.invertTree(root.right)
        
        # Return the current root node, which now represents a fully inverted tree
        return root
