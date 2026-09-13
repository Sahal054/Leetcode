"""
105. Construct Binary Tree from Preorder and Inorder Traversal (Pass-by-Reference Optimization)

--- Bug Alert & Correction ---
The code you provided contains a very common, sneaky bug! 
You used `preorder.pop()`, which removes the element from the END of the list. However, 
in a Preorder traversal [Root, Left, Right], the root is always at the BEGINNING (index 0). 
If you pop from the end, you are grabbing a leaf node from the right subtree instead of the root!

To fix this for Preorder, you must use `preorder.pop(0)`. 
(Note: If you were actually trying to solve LeetCode 106: Postorder and Inorder, `pop()` 
from the end is correct, but you would need to build `root.right` BEFORE `root.left`).

--- The Core Intuition ---
1. The Slicing Problem: In the previous solution, doing `preorder[1:mid+1]` forced Python 
   to create a brand new array copy in memory for every single recursive call. 
2. The Pass-by-Reference Trick: Instead of slicing `preorder`, we pass the EXACT SAME list 
   to every recursive call. 
3. The Pop Mechanism: Because lists in Python are mutable (passed by reference), when we 
   do `preorder.pop(0)`, it permanently removes the root for all future recursive calls. 
   By the time we call `buildTree` for the left child, the first item in the `preorder` 
   list is naturally the left child's root!
4. Inorder Still Slices: We are still slicing the `inorder` array to give the left and 
   right boundaries, so this isn't fully optimized to O(N) yet, but it's a step in the 
   right direction.

--- Visual Traversal Walkthrough ---

Example: 
preorder = [3, 9, 20, 15, 7]  (Shared mutable list)
inorder  = [9, 3, 15, 20, 7]

[ INITIAL CALL ]
- Pop index 0: Root is 3. 
- preorder is permanently mutated to: [9, 20, 15, 7]
- Find 3 in inorder -> mid = 1.
- Call Left: buildTree(preorder, [9])
- Call Right: buildTree(preorder, [15, 20, 7])

[ LEFT SUBTREE CALL ]
- Pop index 0: Root is 9. 
- preorder is mutated to: [20, 15, 7]  <-- Notice how 9 is gone!
- mid = 0.
- Call Left: buildTree(preorder, []) -> Returns None
- Call Right: buildTree(preorder, []) -> Returns None
- Returns Node(9).

[ RIGHT SUBTREE CALL ]
- The right branch now looks at preorder. Thanks to the left branch popping '9', 
  the list is perfectly set up as [20, 15, 7].
- Pop index 0: Root is 20. 
- preorder is mutated to: [15, 7]
- (Continues to build 15 and 7...)

--- Complexity ---
- Time Complexity: $O(N^2)$. While we stopped slicing `preorder`, `preorder.pop(0)` forces 
  all remaining elements in the list to shift left, which takes $O(N)$ time. We also still 
  have `inorder.index()` which takes $O(N)$, making the overall time $O(N^2)$.
- Space Complexity: $O(N^2)$. We are still slicing `inorder[:mid]`, creating new arrays 
  at every step.
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
        # Base case
        if not preorder or not inorder:
            return None
        
        # CORRECTED: Use pop(0) to get the first element for Preorder traversal
        root = TreeNode(preorder.pop(0))
        
        # Find the root's position in the inorder array
        mid = inorder.index(root.val)
        
        # Pass the mutated preorder list by reference. 
        # The left branch will eat its required nodes, leaving the rest for the right branch.
        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid+1:])
    
        return root









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
