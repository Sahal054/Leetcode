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


