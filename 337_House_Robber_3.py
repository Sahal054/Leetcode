"""
337. House Robber III (Tree Dynamic Programming via Postorder DFS)

The objective is to find the maximum money you can rob from houses arranged in a 
binary tree structure. The constraint remains: you cannot rob two directly linked 
parent-child houses on the same night.

--- The Core Intuition: The Power of the Pair ---
Instead of just returning a single number, each node returns a pair of values 
representing two sub-problems:
    [withRoot, withoutRoot]

Index 0 (withRoot): The max money gained if we CHOOSE to rob this current node.
Index 1 (withoutRoot): The max money gained if we CHOOSE to skip this current node.

--- Recurrence Relations ---
For any given node, we look at the pairs returned by its left child and right child:
    leftPair = [leftWith, leftWithout]
    rightPair = [rightWith, rightWithout]

1. If we ROB the current node:
   We CANNOT rob its immediate children. We must take the "without" options from both.
   $$withRoot = \text{root.val} + \text{leftPair}[1] + \text{rightPair}[1]$$

2. If we SKIP the current node:
   We are free to either rob or skip its children—whichever choice yields more money 
   for each respective subtree!
   $$withoutRoot = \max(\text{leftPair}) + \max(\text{rightPair})$$



--- Visual Logic & Step-by-Step Trace ---

Example Tree:
          3
         / \
        2   3
         \   \
          3   1

We evaluate from the bottom up (Postorder Traversal: Left -> Right -> Root):

1. Suffix Leaves (None nodes):
   - Return [0, 0]

2. Node 3 (Right grandchild under 2):
   - Left child = None ([0, 0]), Right child = None ([0, 0])
   - withRoot = 3 + 0 + 0 = 3
   - withoutRoot = max([0,0]) + max([0,0]) = 0
   - Returns: [3, 0]

3. Node 1 (Right grandchild under 3):
   - Left child = None ([0, 0]), Right child = None ([0, 0])
   - withRoot = 1 + 0 + 0 = 1
   - withoutRoot = max([0,0]) + max([0,0]) = 0
   - Returns: [1, 0]

4. Node 2 (Left child of root):
   - Left child = None ([0, 0]), Right child = Node 3 ([3, 0])
   - withRoot = 2 + 0 (leftWithout) + 0 (rightWithout) = 2
   - withoutRoot = max([0,0]) + max([3,0]) = 0 + 3 = 3
   - Returns: [2, 3]

5. Node 3 (Right child of root):
   - Left child = None ([0,0]), Right child = Node 1 ([1, 0])
   - withRoot = 3 + 0 (leftWithout) + 0 (rightWithout) = 3
   - withoutRoot = max([0,0]) + max([1,0]) = 0 + 1 = 1
   - Returns: [3, 1]

6. Root Node 3:
   - Left child = Node 2 ([2, 3]), Right child = Node 3 ([3, 1])
   - withRoot = 3 + 3 (leftWithout) + 1 (rightWithout) = 7  (Robs: Root + Grandchildren)
   - withoutRoot = max([2,3]) + max([3,1]) = 3 + 3 = 6      (Robs: Children)
   - Returns: [7, 6]

Final Choice: max([7, 6]) = 7

--- Complexity ---
- Time Complexity: O(n) since we visit every node exactly once.
- Space Complexity: O(h) where h is the height of the tree, representing the 
  memory utilized by the recursion call stack.
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            # Base case: An empty tree node yields no money
            if not root:
                return [0, 0]
            
            # Bottom-up processing: Collect data from subtrees first
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            # Decision 1: Rob this house -> Cannot rob immediate children
            withRoot = root.val + leftPair[1] + rightPair[1]
            
            # Decision 2: Skip this house -> Take the absolute best from children subtrees
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
        
        # The ultimate answer is the best option available at the absolute root node
        return max(dfs(root))
