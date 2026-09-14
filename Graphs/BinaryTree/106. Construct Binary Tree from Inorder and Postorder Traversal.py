"""
106. Construct Binary Tree from Inorder and Postorder Traversal

--- The Core Intuition ---
1. The Postorder Cheat Code: Postorder traversal follows the pattern [Left, Right, Root]. 
   This means the very LAST element in the `postorder` array is ALWAYS the root of the 
   current tree (or subtree). 
2. Reading Backwards: If we use `postorder.pop()`, we are reading the array from right 
   to left. Reading [Left, Right, Root] backwards gives us the pattern [Root, Right, Left].
3. The Critical Ordering: Because of this [Root, Right, Left] pattern, after we pop 
   the root, the very next numbers in the list belong to the RIGHT subtree. Therefore, 
   we MUST recursively build `root.right` BEFORE `root.left`. If you build the left 
   side first, the tree will grab the wrong nodes and fail completely!
4. The Inorder Split: Just like the Preorder version, finding the root's value inside 
   the `inorder` array tells us exactly which nodes belong to the left subtree (everything 
   before the root) and the right subtree (everything after).

--- Visual Traversal Walkthrough ---

Example: 
inorder   = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]  (Shared mutable list)

[ INITIAL CALL ]
- Pop last element: Root is 3. 
- postorder is mutated to: [9, 15, 7, 20]
- Find 3 in inorder -> mid = 1.
- Call RIGHT FIRST: buildTree(in=[15, 20, 7], postorder)
- Call LEFT SECOND: buildTree(in=[9], postorder)

[ RIGHT SUBTREE CALL ]
- postorder is currently [9, 15, 7, 20].
- Pop last element: Root is 20. 
- postorder is mutated to: [9, 15, 7]
- Find 20 in inorder -> mid = 1 (relative to the slice [15, 20, 7]).
- Call Right: buildTree(in=[7], postorder) -> pops 7, returns Node(7)
- Call Left: buildTree(in=[15], postorder) -> pops 15, returns Node(15)
- Returns Node(20).

[ LEFT SUBTREE CALL ]
- The right branch finished its work. postorder is perfectly set up as [9].
- Pop last element: Root is 9.
- Returns Node(9).

[ END ]
- Both branches are attached.
* Final Tree:
      3
     / \
    9  20
      /  \
     15   7

--- Complexity ---
- Time Complexity: $O(N^2)$. While `postorder.pop()` is incredibly fast ($O(1)$ compared 
  to the $O(N)$ of `preorder.pop(0)`), we are still searching for the root using 
  `inorder.index()`, which takes $O(N)$ time. We do this for every node, making it $O(N^2)$.
- Space Complexity: $O(N^2)$. We are still slicing the `inorder` array (`inorder[:mid]`), 
  which allocates brand new array copies in memory for every single recursive call.
"""

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base case: if there are no nodes in the inorder slice, this branch is empty
        if not inorder:
            return None
        
        # In Postorder, the root is always at the very end. 
        # pop() removes it from the list in O(1) time.
        root = TreeNode(postorder.pop())
        
        # Find the root's position in the inorder array to divide left/right subtrees
        mid = inorder.index(root.val)

        # CRITICAL: We MUST build the right child first! 
        # Because we are popping from the end of a postorder list, the next 
        # available elements belong to the right subtree.
        root.right = self.buildTree(inorder[mid+1:], postorder)
        
        # Once the right child eats all its nodes from the postorder list, 
        # we can safely build the left child.
        root.left = self.buildTree(inorder[:mid], postorder)

        # Return the fully constructed root
        return root
