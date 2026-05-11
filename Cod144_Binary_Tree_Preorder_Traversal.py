"""
Binary Tree Preorder Traversal (Depth-First Search)

In Preorder traversal, we visit nodes in the following order: 
Root -> Left Subtree -> Right Subtree.

This implementation uses a recursive helper function 'traverse' that dives deep 
into the left branches before backtracking to the right branches.


Example Tree:
      1
     / \
    2   3
   / \
  4   5

Step-by-step execution:
Initially: res = []

1. Call traverse(Node 1):
   - Visit Root: append 1 to res. (res = [1])
   - Go Left: call traverse(Node 2).

2. Inside traverse(Node 2):
   - Visit Root: append 2 to res. (res = [1, 2])
   - Go Left: call traverse(Node 4).

3. Inside traverse(Node 4):
   - Visit Root: append 4 to res. (res = [1, 2, 4])
   - No left or right children. Function returns back to Node 2.

4. Back in traverse(Node 2):
   - Go Right: call traverse(Node 5).

5. Inside traverse(Node 5):
   - Visit Root: append 5 to res. (res = [1, 2, 4, 5])
   - No left or right children. Function returns back to Node 2.
   - Node 2 is finished, returns back to Node 1.

6. Back in traverse(Node 1):
   - Go Right: call traverse(Node 3).

7. Inside traverse(Node 3):
   - Visit Root: append 3 to res. (res = [1, 2, 4, 5, 3])
   - No left or right children. Function returns back to Node 1.

Final Result: [1, 2, 4, 5, 3]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]

        def  traverse(current_node):
            if not current_node:
                return            
            res.append(current_node.val)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(root)
        return res 
                        
"""
Iterative Preorder Traversal (Depth-First Search)

This version uses an explicit Stack instead of recursion to simulate the 
backtracking process. The strategy is to visit the Root, push the Right child 
onto the stack for later, and immediately move to the Left child.

Example Tree:
      1
     / \
    2   3
   / \
  4   5

Logic: 
- Root -> Left -> Right
- We keep moving left as far as possible. 
- The stack "remembers" the right branches we skipped so we can return to them.



Step-by-step execution:
Initially: cur = Node 1, stack = [], res = []

--- Iteration 1 ---
- 'cur' exists (Node 1):
    - Append 1 to res: res = [1]
    - Push right child (Node 3) to stack: stack = [Node 3]
    - Move cur to left: cur = Node 2

--- Iteration 2 ---
- 'cur' exists (Node 2):
    - Append 2 to res: res = [1, 2]
    - Push right child (Node 5) to stack: stack = [Node 3, Node 5]
    - Move cur to left: cur = Node 4

--- Iteration 3 ---
- 'cur' exists (Node 4):
    - Append 4 to res: res = [1, 2, 4]
    - Push right child (None) to stack: stack = [Node 3, Node 5, None]
    - Move cur to left: cur = None

--- Iteration 4 ---
- 'cur' is None (hit a dead end):
    - Pop from stack: cur = None, stack = [Node 3, Node 5]

--- Iteration 5 ---
- 'cur' is still None:
    - Pop from stack: cur = Node 5, stack = [Node 3]

--- Iteration 6 ---
- 'cur' exists (Node 5):
    - Append 5 to res: res = [1, 2, 4, 5]
    - Push right child (None) to stack: stack = [Node 3, None]
    - Move cur to left: cur = None

--- Iteration 7 ---
- 'cur' is None:
    - Pop from stack: cur = None, stack = [Node 3]

--- Iteration 8 ---
- 'cur' is None:
    - Pop from stack: cur = Node 3, stack = []

--- Iteration 9 ---
- 'cur' exists (Node 3):
    - Append 3 to res: res = [1, 2, 4, 5, 3]
    - Push right child (None) to stack: stack = [None]
    - Move cur to left: cur = None

--- Iteration 10 ---
- 'cur' is None:
    - Pop from stack: cur = None, stack = []

Loop ends because both 'stack' and 'cur' are empty/None.
Final Result: [1, 2, 4, 5, 3]
"""



class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stack =[]
        res =[]

        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur= cur.left
            else:
                cur = stack.pop()  
        return res           











