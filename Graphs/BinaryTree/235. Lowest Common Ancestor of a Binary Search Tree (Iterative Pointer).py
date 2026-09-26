"""
235. Lowest Common Ancestor of a Binary Search Tree (Iterative Pointer)

--- The Core Intuition ---
1. The BST Property: This problem gives you a Binary Search Tree, not a regular binary tree. 
   This is a massive advantage! We know that everything to the left of a node is smaller, 
   and everything to the right is larger.
2. Finding the "Split Point": The Lowest Common Ancestor (LCA) is simply the very first 
   node where the paths to `p` and `q` diverge (one goes left, the other goes right).
3. The Three Scenarios:
   - If both `p` and `q` are GREATER than our current node, they are both hiding 
     somewhere in the right subtree. We step right.
   - If both `p` and `q` are LESS than our current node, they are both hiding 
     somewhere in the left subtree. We step left.
   - If one is greater and one is less (or if one of them is exactly equal to the 
     current node), we have found the exact intersection where their paths split! 
     The current node is the LCA.

--- Visual Traversal Walkthrough ---

Example: 
         6
       /   \
      2     8
     / \   / \
    0   4 7   9
       / \
      3   5

Target 1: p = 2, q = 4

[ INITIAL SETUP ]
- curr = 6

[ LOOP 1: curr = 6 ]
- Is p(2) > 6 AND q(4) > 6? No.
- Is p(2) < 6 AND q(4) < 6? YES.
- Move left: curr = curr.left (Node 2)

[ LOOP 2: curr = 2 ]
- Is p(2) > 2 AND q(4) > 2? No.
- Is p(2) < 2 AND q(4) < 2? No. 
  (Because p is exactly equal to 2, it is not strictly less than 2).
- Hits the `else` block. 
- The paths have split (or rather, one target IS the LCA of the other).
- Return Node 2.

--- Complexity ---
- Time Complexity: $O(H)$ where $H$ is the height of the tree. We only traverse down a 
  single path from the root to the LCA. In a perfectly balanced BST, this is $O(\log N)$. 
  In the worst-case scenario (a linked-list-like skewed tree), it is $O(N)$.
- Space Complexity: $O(1)$. Because you solved this iteratively using a `while` loop 
  instead of recursion, you completely avoided the recursive call stack. You only use 
  a single `curr` pointer, resulting in strict, constant memory usage.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start our pointer at the root
        curr = root

        # Traverse down the tree
        while curr:
            # If both targets are greater, the LCA must be to the right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                
            # If both targets are smaller, the LCA must be to the left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
                
            # If one is greater and one is less, OR if we land exactly on p or q,
            # we have found the point of divergence. This is the LCA.
            else:
                return curr
