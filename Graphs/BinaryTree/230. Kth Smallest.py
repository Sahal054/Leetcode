"""
230. Kth Smallest Element in a BST (Inorder DFS)

--- The Core Intuition ---
1. The Inorder Cheat Code: Because this is a Binary Search Tree, an Inorder traversal 
   (Left, Root, Right) will always visit the nodes in strictly ascending, sorted order. 
   The 1st node we process is the absolute smallest, the 2nd is the 2nd smallest, and so on.
2. The Counter: We don't need to store the entire sorted tree in an array. We just need 
   to keep a running counter (`self.n`). Every time we finish exploring a left branch 
   and finally stand on a root node to process it, we increment our counter by 1.
3. The Target: The moment our counter `self.n` perfectly equals `k`, we have found our 
   target! We save that node's value into `self.res` and return to stop exploring deeper 
   down that specific path.

--- Visual Traversal Walkthrough ---

Example: k = 3
       5
      / \
     3   6
    / \
   2   4

[ INITIAL SETUP ]
- self.n = 0
- self.res = 0
- dfs(root=5, k=3)

[ DIVING LEFT ]
- Node 5 has a left child. dfs(3).
- Node 3 has a left child. dfs(2).
- Node 2 does not have a left child. 

[ PROCESSING NODES ]
- (At Node 2): 
  - self.n += 1 -> self.n is now 1. (1 != 3)
  - No right child. Return to Node 3.
- (At Node 3): 
  - self.n += 1 -> self.n is now 2. (2 != 3)
  - Has right child. dfs(4).
- (At Node 4):
  - No left child.
  - self.n += 1 -> self.n is now 3. 
  - self.n == k! 
  - self.res = 4. Return immediately!

[ BACKTRACKING ]
- The function bubbles back up, but `self.res` is safely locked in as 4.

[ END ]
- Return self.res, which is 4.

--- Complexity ---
- Time Complexity: O(H + k) where H is the height of the tree. We must travel down to 
  the leftmost leaf (which takes O(H) time) and then process k nodes. In the absolute 
  worst-case (a completely unbalanced, left-skewed tree where k = N), this becomes O(N).
- Space Complexity: O(H) to account for the recursive call stack. In a perfectly 
  balanced tree, this is O(log N). In a worst-case skewed tree, it degrades to O(N).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        self.n  = 0
        self.res = 0

        def dfs(root,k):
            if not root:
                return 
            
            if root.left:
                dfs(root.left,k)
            
            self.n+=1

            if self.n == k:
                self.res = root.val
                return 

            if root.right:
                dfs(root.right,k)
        
        (dfs(root,k))
        return self.res
