"""
Binary Tree Postorder Traversal (Recursive Depth-First Search)

In Postorder traversal, we visit nodes in the following order: 
Left Subtree -> Right Subtree -> Root.

The "Post" means the root is processed AFTER its children. This is very 
useful for tasks like deleting a tree or evaluating mathematical expressions, 
where you need the child values before you can calculate the parent.



Example Tree:
      1
     / \
    2   3
   / \
  4   5

Step-by-step execution:
Initially: res = []

1. Call traverse(Node 1):
   - Go Left: call traverse(Node 2).

2. Inside traverse(Node 2):
   - Go Left: call traverse(Node 4).

3. Inside traverse(Node 4):
   - No children. 
   - Visit Root: append 4 to res. (res = [4])
   - Return to Node 2.

4. Back in traverse(Node 2):
   - Go Right: call traverse(Node 5).

5. Inside traverse(Node 5):
   - No children.
   - Visit Root: append 5 to res. (res = [4, 5])
   - Return to Node 2.

6. Back in traverse(Node 2):
   - Both children done.
   - Visit Root: append 2 to res. (res = [4, 5, 2])
   - Return to Node 1.

7. Back in traverse(Node 1):
   - Go Right: call traverse(Node 3).

8. Inside traverse(Node 3):
   - No children.
   - Visit Root: append 3 to res. (res = [4, 5, 2, 3])
   - Return to Node 1.

9. Back in traverse(Node 1):
   - Both children done.
   - Visit Root: append 1 to res. (res = [4, 5, 2, 3, 1])

Final Result: [4, 5, 2, 3, 1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res =[]
        def traverse(current_node):
            if not current_node:
                return 
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            res.append(current_node.val)
        traverse(root)
        return res             
