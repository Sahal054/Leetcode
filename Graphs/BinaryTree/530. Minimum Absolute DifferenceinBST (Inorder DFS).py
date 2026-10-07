"""
530. Minimum Absolute Difference in BST (Inorder DFS)

--- The Core Intuition ---
1. The BST Cheat Code (Again): Because this is a Binary Search Tree, an Inorder 
   Traversal (Left, Root, Right) will naturally visit the nodes in strictly 
   ascending, sorted order.
2. Adjacent Differences: The minimum absolute difference between ANY two numbers 
   in a sorted list must always be between two numbers that are right next to each 
   other. We don't need to compare every single node against every other node—we 
   only need to compare the current node to the node we visited immediately before it.
3. The "Previous" Tracker: We maintain a `prev` variable to remember the value of 
   the last node we processed. As we move to the next node in the inorder sequence, 
   we calculate the difference, update our global minimum, and then update `prev` 
   to the current node's value.

--- Visual Traversal Walkthrough ---

Example: 
       4
      / \
     2   6
    / \
   1   3

[ INITIAL SETUP ]
- prev = None
- min_diff = Infinity
- Inorder Traversal begins (Dive all the way left to Node 1)

[ PROCESSING NODE 1 ]
- node = 1.
- prev is None, so we can't calculate a difference yet.
- Update prev = 1.
- Move right (None), return to Node 2.

[ PROCESSING NODE 2 ]
- node = 2. 
- prev is 1. Difference: 2 - 1 = 1.
- min_diff = min(Infinity, 1) = 1.
- Update prev = 2.
- Move right to Node 3.

[ PROCESSING NODE 3 ]
- node = 3.
- prev is 2. Difference: 3 - 2 = 1.
- min_diff = min(1, 1) = 1.
- Update prev = 3.
- Return to Root Node 4.

[ PROCESSING NODE 4 ]
- node = 4.
- prev is 3. Difference: 4 - 3 = 1.
- min_diff = min(1, 1) = 1.
- Update prev = 4.
- Move right to Node 6.

[ PROCESSING NODE 6 ]
- node = 6. Dive left (None).
- prev is 4. Difference: 6 - 4 = 2.
- min_diff = min(1, 2) = 1.
- Update prev = 6.

[ END ]
- Return min_diff, which is 1.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes in the tree. We visit 
  every node exactly once during the traversal.
- Space Complexity: $O(H)$ where $H$ is the height of the tree. This accounts for 
   the recursive call stack. In a perfectly balanced tree, this is $O(\log N)$. 
  In a worst-case skewed tree, it becomes $O(N)$.
"""

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Use instance variables to track state across recursive calls
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            
            # 1. Traverse all the way down the left branch (smaller values)
            inorder(node.left)

            # 2. Process the current root node
            if self.prev is not None:
                # Calculate difference between current node and the previous node in the sorted sequence
                self.min_diff = min(self.min_diff, node.val - self.prev)
            
            # Update prev to the current node before moving on
            self.prev = node.val

            # 3. Traverse down the right branch (larger values)
            inorder(node.right)
        
        inorder(root)
        
        return int(self.min_diff)
