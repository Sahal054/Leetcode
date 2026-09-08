"""
112. Path Sum (Recursive Depth-First Search)

--- The Core Intuition ---
1. Accumulating State: As we traverse down the tree, we need to remember the sum of 
   the nodes we've seen so far. We pass this running total (`currSum`) down to our 
   children via the recursive `dfs` function.
2. The Leaf Node Rule: The problem strictly defines a path as going from the root 
   down to a LEAF. A leaf is a node with absolutely no children. We only check if we 
   hit the `targetSum` when we are standing on a leaf. 
3. The OR Logic: We don't need every path to equal the target sum—we just need ONE. 
   By returning `dfs(left) or dfs(right)`, if any single path deep in the tree finds 
   a match and returns `True`, that `True` will instantly bubble all the way back up 
   to the root.
4. Handling Nulls: If we hit a `None` node, it means the path ended without being a 
   leaf (or the tree itself is empty). We just return `False` so it doesn't affect the 
   other valid branches.

--- Visual Traversal Walkthrough ---

Example: targetSum = 22
         5
        / \
       4   8
      /   / \
    11  13   4
   /  \       \
  7    2       1

[ INITIAL CALL ]
- dfs(root=5, currSum=0)
- Add 5. currSum = 5.
- Not a leaf. Branch out: dfs(4, 5) OR dfs(8, 5)

[ GOING DOWN THE LEFT BRANCH ]
- dfs(4, 5): Add 4. currSum = 9.
  Not a leaf. Branch left: dfs(11, 9)
- dfs(11, 9): Add 11. currSum = 20.
  Not a leaf. Branch out: dfs(7, 20) OR dfs(2, 20)

[ CHECKING THE LEAVES ]
- dfs(7, 20): Add 7. currSum = 27.
  Is it a leaf? YES. Does 27 == 22? NO. Returns False.
- dfs(2, 20): Add 2. currSum = 22.
  Is it a leaf? YES. Does 22 == 22? YES! Returns True.

[ BUBBLING UP ]
- Node 11 returns (False OR True) -> True
- Node 4 returns True
- Root 5 returns True. We found our path! (5 -> 4 -> 11 -> 2)

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes in the tree. In the worst-case 
  scenario (if the tree does not contain the target sum), we have to visit every single 
  node exactly once to be sure.
- Space Complexity: $O(H)$ where $H$ is the height of the tree. This is the space taken 
  by the recursive call stack. In a perfectly balanced tree, this is $O(\log N)$. In a 
  completely unbalanced, single-line tree, it becomes $O(N)$.
"""

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Helper function to carry the running sum downward
        def dfs(node, currSum):
            # Base case: We reached a dead end. This path failed.
            if not node:
                return False
            
            # Add the current node's value to our running total
            currSum += node.val

            # Check if we are currently standing on a leaf node
            if not node.left and not node.right:
                # If we are at a leaf, verify if our total matches the target
                return currSum == targetSum
            
            # If not a leaf, continue searching down both the left and right paths.
            # If EITHER path finds the target, return True.
            return (dfs(node.left, currSum) or dfs(node.right, currSum))
    
        # Start the traversal at the root with an initial sum of 0
        return dfs(root, 0)
