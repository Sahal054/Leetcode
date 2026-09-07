"""
105. Construct Binary Tree from Preorder and Inorder Traversal

--- The Core Intuition ---
1. The Preorder Cheat Code: Preorder traversal always follows the pattern [Root, Left, Right]. 
   This means the very first element in the `preorder` array is ALWAYS the root of the 
   current tree (or subtree).
2. The Inorder Map: Inorder traversal follows the pattern [Left, Root, Right]. Once we 
   know what the root is (thanks to preorder), we can find that root inside the `inorder` array.
3. The Split: Everything to the left of the root in the `inorder` array belongs to the 
   Left Subtree. Everything to the right belongs to the Right Subtree. 
4. The Recursive Build: By finding the root's index (`mid`) in the `inorder` array, we 
   know exactly how many nodes are in the left subtree. We can then slice both arrays 
   and pass those chunks down recursively to build the left and right branches.

--- Visual Traversal Walkthrough ---

Example: 
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

[ INITIAL CALL ]
- preorder[0] is 3. Root is 3.
- Find 3 in inorder: it's at index 1 (`mid = 1`).
- Left subtree size is 1. Right subtree size is 3.
- Build Left: buildTree(pre=[9], in=[9])
- Build Right: buildTree(pre=[20, 15, 7], in=[15, 20, 7])

[ LEFT SUBTREE CALL ]
- preorder = [9], inorder = [9]
- Root is 9. `mid = 0`.
- Left and Right slices become empty lists.
- Returns Node(9). 
* Tree so far:
      3
     /
    9

[ RIGHT SUBTREE CALL ]
- preorder = [20, 15, 7], inorder = [15, 20, 7]
- Root is 20. Find 20 in inorder -> `mid = 1`.
- Build Left: buildTree(pre=[15], in=[15]) -> Returns Node(15)
- Build Right: buildTree(pre=[7], in=[7]) -> Returns Node(7)
- Returns Node(20).

[ END ]
- Both branches are attached to the root.
* Final Tree:
      3
     / \
    9  20
      /  \
     15   7

--- Complexity ---
- Time Complexity: $O(N^2)$ in the worst case. Finding the root using `inorder.index()` 
  takes $O(N)$ time, and we do this for every node. Furthermore, list slicing in Python 
  (e.g., `preorder[1:mid+1]`) creates brand new array copies, which takes $O(N)$ time 
  at every step. 
- Space Complexity: $O(N^2)$ because we are constantly creating new sub-arrays in memory 
  for every recursive call. 
"""

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: If either array is empty, there are no nodes left to build.
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is ALWAYS the root of the current subtree
        root = TreeNode(preorder[0])
        
        # Find the index of the root in the inorder array. 
        # This tells us how many nodes are in the left subtree.
        mid = inorder.index(preorder[0])
        
        # Recursively build the left subtree.
        # Preorder slice: start at 1, take 'mid' elements -> preorder[1:mid+1]
        # Inorder slice: take everything before 'mid' -> inorder[:mid]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Recursively build the right subtree.
        # Preorder slice: take everything after the left subtree's elements -> preorder[mid+1:]
        # Inorder slice: take everything after the root -> inorder[mid+1:]
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # Return the fully constructed root node to attach it to its parent
        return root
