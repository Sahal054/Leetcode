"""
98. Validate Binary Search Tree (Recursive DFS / Boundary Tracking)

--- The Core Intuition ---
1. The Grandparent Problem: A common mistake is to only check if a node is less than 
   its direct parent or greater than its direct parent. However, in a valid BST, a node 
   deep in a left subtree must STILL be strictly less than the absolute root of the tree.
2. The Bounding Box: To solve this, we create a strict "bounding box" of valid numbers 
   `(left, right)` and pass it down the tree. A node's value MUST fall inside this box.
3. Shrinking the Boundaries: 
   - When we travel down a LEFT branch, all values must be smaller than the current 
     node. So, the current node's value becomes the new strict maximum (`right` boundary).
   - When we travel down a RIGHT branch, all values must be larger than the current 
     node. So, the current node's value becomes the new strict minimum (`left` boundary).
4. The Base Cases: If we hit a `None` node, it's valid. If any node's value falls 
   outside its bounding box, we immediately return `False`.

--- Visual Traversal Walkthrough ---

Example: 
      5
     / \
    4   6
       / \
      3   7

(Notice the 3! It is smaller than 6, which seems fine locally, but it is in the 
RIGHT subtree of the root 5. It should be greater than 5.)

[ INITIAL CALL ]
- dfs(root=5, left=-infinity, right=infinity)
- Is 5 between -inf and inf? YES.
- Call Left: dfs(4, -inf, 5)
- Call Right: dfs(6, 5, inf)

[ LEFT BRANCH ]
- dfs(4, -inf, 5)
- Is 4 between -inf and 5? YES.
- Both children are None (returns True). 

[ RIGHT BRANCH ]
- dfs(6, 5, inf)
- Is 6 between 5 and inf? YES.
- Call Left: dfs(3, 5, 6)   <-- BOUNDARY SHRUNK!
- Call Right: dfs(7, 6, inf)

[ THE VIOLATION (Node 3) ]
- dfs(3, 5, 6)
- Is 3 greater than 5 AND less than 6? NO!
- Returns False. The False bubbles all the way up.

--- Complexity ---
- Time Complexity: O(N) where N is the number of nodes in the tree. In the worst-case 
  scenario, we must visit every single node exactly once.
- Space Complexity: O(H) where H is the height of the tree for the recursive call stack. 
  In a balanced BST, this is O(log N).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(root , left, right):
            if not root:
                return True
            
            if not(root.val > left and root.val < right):
                return False
            

            return( dfs(root.left, left, root.val) and
                    dfs (root.right, root.val, right))
            
        return dfs(root, float("-inf"),float("inf"))
