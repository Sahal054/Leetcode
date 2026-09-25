"""
124. Binary Tree Maximum Path Sum (Post-order DFS)

--- The Core Intuition ---
1. The Definition of a Path: A path can go up, down, or sideways, but it can never 
   fork. You cannot traverse a node, go down its left branch, come back up, and then 
   go down its right branch as part of a continuous line returned to the parent.
2. The "Split" vs. The "Straight Line": At every single node, you must make a choice:
   - The Split (Global Max): You treat the current node as the absolute peak/arch of 
     the path. The path goes up the left child, through the current node, and down 
     the right child. You calculate this total and check if it's the highest sum 
     you've seen so far across the entire tree, updating `res[0]`.
   - The Straight Line (Return Value): Because a path cannot fork, when the function 
     returns to its parent, it can only offer ONE branch. It must choose the best 
     single path (either left or right) plus the current node's value.
3. Toxic Branches (Negative Filtering): If a subtree's maximum path sum is negative, 
   adding it to your current path will only drag your total down. We use `max(..., 0)` 
   to completely ignore negative branches, effectively saying, "If you bring me down, 
   I just won't include you in my path at all."

--- Visual Traversal Walkthrough ---

Example: 
       -10
       /  \
      9   20
         /  \
        15   7

[ INITIAL SETUP ]
- res = [-10] (Initial global max is the root)
- Call dfs(-10)

[ LEFT BRANCH OF ROOT ]
- dfs(9):
  - Leaf node. Left = 0, Right = 0.
  - Split: 0 + 0 + 9 = 9. Update res = [9].
  - Returns: 9 + max(0,0) = 9.

[ RIGHT BRANCH OF ROOT: Node 20 ]
- dfs(20) needs left and right children first.
  - dfs(15): Split = 15. Update res = [15]. Returns 15.
  - dfs(7):  Split = 7.  res remains [15]. Returns 7.
- Back at Node 20: 
  - leftmax = max(15, 0) = 15
  - rightmax = max(7, 0) = 7
  - Split: 15 + 7 + 20 = 42. Update res = [42]!
  - Returns straight line: 20 + max(15, 7) = 35.

[ ROOT NODE: -10 ]
- leftmax = max(9, 0) = 9
- rightmax = max(35, 0) = 35
- Split: 9 + 35 + (-10) = 34. (34 is not greater than 42, res stays [42]).
- Returns: -10 + max(9, 35) = 25. (Though this return value isn't used by anything).

[ END ]
- We return res[0], which caught the peak value of 42 deep inside the right subtree.

--- Complexity ---
- Time Complexity: O(N) where N is the number of nodes in the tree. We visit every 
  node exactly once doing constant-time math operations at each stop.
- Space Complexity: O(H) where H is the height of the tree. This is the memory used 
  by the recursive call stack. In the worst-case scenario (a skewed tree), this is O(N).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # We use a list to store the global maximum so it can be mutated inside dfs
        res = [root.val]
        
        def dfs(node):
            # Base case: empty nodes contribute 0 to a path sum
            if not node:
                return 0
            
            # Post-order traversal: Get the max path sums from left and right children
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)

            # Ignore negative branches. If a branch is toxic (< 0), treat it as 0
            rightmax = max(rightmax, 0)
            leftmax = max(leftmax, 0)

            # CALCULATE THE SPLIT: What if this node is the highest point of our path?
            # Update the global maximum if this inverted U-shape path is the best so far.
            res[0] = max(res[0], leftmax + rightmax + node.val)

            # CALCULATE THE STRAIGHT LINE: What can we pass up to the parent?
            # We can only pass up one contiguous line, so we pick the better child branch.
            return node.val + max(leftmax, rightmax)
        
        # Trigger the recursion
        dfs(root)

        return res[0]
