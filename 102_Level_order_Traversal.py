"""
Level Order Traversal (Breadth-First Search)

The goal is to traverse the tree level-by-level. We use a Queue (First-In-First-Out) 
to achieve this. To group nodes by their specific level, we take a "snapshot" of the 
queue's length at the start of each while loop iteration.

Example Tree:
      3
     / \
    9  20
      /  \
     15   7

Step-by-step execution:
(Note: queue stores actual TreeNode objects, numbers below represent those nodes)

Initialization:
queue = [3]
res = []

--- Iteration 1 ---
lenq = 1  (Only the root is in the queue)
Loop i from 0 to 0:
  - Pop 3. level = [3]
  - Add 3's children (9, 20) to queue. 
    queue = [9, 20]
Result so far: res = [[3]]

--- Iteration 2 ---
lenq = 2  (Nodes 9 and 20 are in the queue)
Loop i from 0 to 1:
  i=0: Pop 9.  level = [9]. No children to add. 
       queue = [20]
  i=1: Pop 20. level = [9, 20]. Add 20's children (15, 7) to queue. 
       queue = [15, 7]
Result so far: res = [[3], [9, 20]]

--- Iteration 3 ---
lenq = 2  (Nodes 15 and 7 are in the queue)
Loop i from 0 to 1:
  i=0: Pop 15. level = [15]. No children.
       queue = [7]
  i=1: Pop 7.  level = [15, 7]. No children.
       queue = []
Result so far: res = [[3], [9, 20], [15, 7]]

Queue is now empty, while loop terminates.
Final output: [[3], [9, 20], [15, 7]]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res =[]
        queue = []
        queue.append(root)
        while queue:
            lenq = len(queue)
            level = []

            for i in range(lenq):
                current_node = queue.pop(0)
                level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            if level:
                res.append(level)
        return res                     
