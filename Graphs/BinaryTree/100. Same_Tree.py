"""
100. Same Tree (Recursive Depth-First Search)

--- The Core Intuition ---
1. Simultaneous Traversal: To check if two trees are identical, we must traverse 
   both of them at the exact same time and compare them step-by-step. Depth-First 
   Search (DFS) is perfect for this.
2. The Success Base Case: If both pointers reach a `None` (a leaf's empty child) 
   at the same time, this specific path matches perfectly. Return `True`.
3. The Failure Base Cases: 
   - Structural Mismatch: If one pointer is `None` but the other is a real node, 
     the trees have different shapes. Return `False`. (This is caught by `not p or not q` 
     because the previous `if` statement already handled the case where BOTH are `None`).
   - Value Mismatch: If both are real nodes but `p.val != q.val`, they have 
     different data. Return `False`.
4. The Recursive Step: If the current nodes match in both structure and value, we 
   delegate the rest of the work. We ask: "Is the left subtree identical? AND is 
   the right subtree identical?" Both must be `True` for the whole tree to be `True`.

--- Visual Traversal Walkthrough ---

Example: 
Tree P:      1         Tree Q:      1
            / \                    / \
           2   3                  2   3

[ INITIAL CALL ]
- p = 1, q = 1
- Both exist, and 1 == 1.
- Make recursive call for LEFT children: isSameTree(2, 2)

[ LEFT CHILD CALL ]
- p = 2, q = 2
- Both exist, and 2 == 2.
- Make recursive call for LEFT children: isSameTree(None, None)
  -> Returns True!
- Make recursive call for RIGHT children: isSameTree(None, None)
  -> Returns True!
- Left branch returns (True AND True) -> True.

[ RIGHT CHILD CALL ]
- Back at the root, we now check the RIGHT children: isSameTree(3, 3)
- p = 3, q = 3
- Both exist, and 3 == 3.
- Left children: isSameTree(None, None) -> True
- Right children: isSameTree(None, None) -> True
- Right branch returns (True AND True) -> True.

[ END ]
- Root returns (Left branch True AND Right branch True) -> True.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes in the smaller of the two 
  trees. We visit every matching node exactly once. The moment we find a mismatch, 
  the recursion cuts off early.
- Space Complexity: $O(H)$ where $H$ is the height of the tree. This is the memory 
  used by the recursive call stack. In a perfectly balanced tree, this is $O(\log N)$. 
  In the worst-case scenario (a completely unbalanced, straight-line tree), it 
  deteriorates to $O(N)$.
"""

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are null. They match perfectly.
        if not p and not q:
            return True
            
        # Base case 2: One is null and the other isn't, OR their values don't match.
        # Note: We know they aren't BOTH null here because of the previous check.
        if not p or not q or p.val != q.val:
            return False
        
        # Recursive step: Both the left branches AND right branches must be identical.
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
