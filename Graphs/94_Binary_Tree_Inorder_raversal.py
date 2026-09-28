"""
94. Binary Tree Inorder Traversal (Iterative Stack)

--- The Core Intuition ---
1. Simulating the Call Stack: A recursive inorder traversal (Left, Root, Right) relies on 
   the computer's hidden call stack to remember parent nodes while it travels down the left 
   branches. To do this iteratively, we manually create our own `stack` array to remember 
   the exact same breadcrumb trail.
2. The Leftward Dive: The inner `while curr:` loop represents the "Left" phase. We 
   aggressively dive down the left side of the current branch, pushing every node we touch 
   onto the stack so we don't lose track of it, until we hit a dead end (`None`).
3. Process the Root: When we hit that dead end, we pop the top node off the stack. Because 
   we've exhausted its left branch (or it didn't have one), it is now time for the "Root" 
   phase. We append its value to our results array.
4. The Right Turn: After processing the node, we move to the "Right" phase by setting 
   `curr = curr.right`. 
   - If a right child exists, the next iteration of the loop will dive down its left side.
   - If a right child doesn't exist (`curr` becomes `None`), the outer loop will just pop 
     the next ancestor off the stack and process it.

--- Visual Traversal Walkthrough ---

Example: 
      1
       \
        2
       /
      3

[ INITIAL SETUP ]
- res = []
- stack = []
- curr = Node(1)

[ ITERATION 1 ]
- Inner loop dives left: Push Node(1). curr becomes None. (stack = [1])
- curr is None, so we pop: curr = Node(1).
- Append to res: res = [1].
- Move right: curr = Node(1).right -> Node(2).

[ ITERATION 2 ]
- Inner loop dives left from Node(2): 
  - Push Node(2). curr -> Node(3). (stack = [2])
  - Push Node(3). curr -> None. (stack = [2, 3])
- curr is None, so we pop: curr = Node(3).
- Append to res: res = [1, 3].
- Move right: curr = Node(3).right -> None.

[ ITERATION 3 ]
- curr is None, inner loop skips.
- Pop from stack: curr = Node(2). (stack = [])
- Append to res: res = [1, 3, 2].
- Move right: curr = Node(2).right -> None.

[ END ]
- curr is None AND stack is empty. Outer loop terminates. 
- Return [1, 3, 2].

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes in the tree. Every single 
  node is pushed onto the stack exactly once and popped off exactly once. 
- Space Complexity: $O(H)$ where $H$ is the height of the tree. This is the maximum 
  number of nodes stored in the stack at any given time. In a balanced tree, this is 
  $O(\log N)$. In a worst-case scenario (a completely left-skewed tree), the stack 
  will hold all $N$ nodes, making it $O(N)$.
"""

from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        
        # Start our pointer at the root
        curr = root
        
        # Continue as long as there are unvisited nodes in the tree OR
        # unprocessed ancestors sitting in our stack
        while curr or stack:

            # 1. Dive as deep as possible down the left branches
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. When we can't go left anymore, pull the last visited node off the stack
            curr = stack.pop()
            
            # 3. Process the node (Inorder means process after exploring left)
            res.append(curr.val)
            
            # 4. Pivot to the right subtree. If it's None, the next loop iteration 
            #    will skip the inner while loop and pop the next ancestor.
            curr = curr.right
            
        return res



"""

This is the same as the post order and pre order just that the results come in the middle refer the 102.


"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]

        def traversal(current_node):
            if not current_node:
                return 
            if current_node.left:
                traversal(current_node.left)
            res.append(current_node.val)
            if current_node.right:
                traversal(current_node.right)
        traversal(root)
        return res 


