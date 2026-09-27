"""
236. Lowest Common Ancestor of a Binary Tree (Recursive DFS)

--- The Core Intuition ---
1. No BST Cheat Codes: Because this is a standard binary tree, we cannot use node 
   values to decide whether to go left or right. We must exhaustively search the 
   tree from the bottom up.
2. The Base Cases: 
   - If we hit a dead end (`None`), we return `None`.
   - If we stumble upon either `p` or `q`, we instantly stop searching that branch 
     and return the node itself. This tells the parent, "Hey, I found one of the 
     targets down this path!"
3. The Intersection (The LCA): When the recursion bubbles back up, every node looks 
   at the results from its left and right children. If a node receives a non-null 
   result from BOTH `left` and `right`, it means `p` is down one branch and `q` is 
   down the other. This makes the current node the exact point of divergence—the LCA! 
   It then returns itself to pass the LCA up the chain.
4. The Pass-Through: If a node only receives a target from ONE of its branches (and 
   `None` from the other), it simply passes that found target further up the tree.

--- Visual Traversal Walkthrough ---

Example: 
         3
       /   \
      5     1
     / \   / \
    6   2 0   8

Target 1: p = 6, Target 2: q = 2

[ INITIAL CALL: Node 3 ]
- dfs(3) is not p or q. Branches out to left (5) and right (1).

[ SEARCHING LEFT BRANCH: Node 5 ]
- dfs(5) is not p or q. Branches out to left (6) and right (2).
  - dfs(6) hits base case (root == p). Returns Node 6.
  - dfs(2) hits base case (root == q). Returns Node 2.
- Back at Node 5: left = Node 6, right = Node 2.
- Both `left` and `right` exist! This means 5 is the LCA. 
- Node 5 returns itself (Node 5) up the chain.

[ SEARCHING RIGHT BRANCH: Node 1 ]
- dfs(1) is not p or q. Branches out to left (0) and right (8).
  - dfs(0) returns None.
  - dfs(8) returns None.
- Back at Node 1: left = None, right = None.
- Returns None up the chain.

[ RESOLUTION AT ROOT: Node 3 ]
- left = Node 5, right = None.
- Because only `left` exists, we execute `return left if left else right`.
- Node 3 passes Node 5 all the way up as the final answer.

--- Complexity ---
- Time Complexity: O(N) where N is the number of nodes in the tree. In the worst-case 
  scenario (where the targets are deep in the tree or one doesn't exist), we have 
  to visit every single node.
- Space Complexity: O(H) where H is the height of the tree. This accounts for the 
  recursive call stack. In a perfectly balanced tree, this is O(log N). In a skewed 
  tree, it is O(N).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case 1: Reached a leaf's empty child
        # Base case 2: We found one of our targets! Return it immediately.
        if not root or root == p or root == q:
            return root
        
        # Search the left subtree for p or q
        left = self.lowestCommonAncestor(root.left, p, q)
        
        # Search the right subtree for p or q
        right = self.lowestCommonAncestor(root.right, p, q)

        # If we found one target in the left branch AND one in the right branch,
        # the current node MUST be the lowest common ancestor.
        if left and right:
            return root
        
        # Otherwise, if we only found a target down one branch, pass it upwards.
        # (If both are None, this naturally returns None).
        return left if left else right
