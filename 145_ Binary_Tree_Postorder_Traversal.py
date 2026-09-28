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



"""
145. Binary Tree Postorder Traversal (Iterative / Reverse Preorder Hack)

--- The Core Intuition ---
1. The Iterative Postorder Challenge: A true iterative Postorder traversal (Left, Right, Root) 
   is notoriously annoying to write. You have to travel down the tree, remember the parent, 
   process the right child, and somehow know whether you are returning from the left branch 
   or the right branch before finally processing the root.
2. The Reversal Hack: Instead of fighting the complex logic of Postorder, we can use a 
   brilliant cheat code. Standard Preorder traversal is [Root, Left, Right]. If we simply 
   tweak Preorder to visit the right child first, we get [Root, Right, Left].
3. The Magic Flip: If you take the sequence [Root, Right, Left] and reverse the entire list 
   backwards, you get exactly [Left, Right, Root] — which is a perfect Postorder traversal!
4. Stack Mechanics: To achieve the [Root, Right, Left] order, we pop the current node and 
   add it to our result. Then, we push the `left` child onto the stack FIRST, followed by 
   the `right` child. Because stacks are Last-In-First-Out (LIFO), the right child will be 
   popped and processed on the very next loop iteration.

--- Visual Traversal Walkthrough ---

Example: 
      1
    /   \
   2     3
  / \
 4   5

[ INITIAL SETUP ]
- stack = [1]
- res = []

[ ITERATION 1: Node 1 ]
- Pop 1. res = [1].
- Push left (2). stack = [2].
- Push right (3). stack = [2, 3].

[ ITERATION 2: Node 3 ]
- Pop 3 (LIFO). res = [1, 3].
- No children to push. stack = [2].

[ ITERATION 3: Node 2 ]
- Pop 2. res = [1, 3, 2].
- Push left (4). stack = [4].
- Push right (5). stack = [4, 5].

[ ITERATION 4 & 5: Leaves 5 and 4 ]
- Pop 5. res = [1, 3, 2, 5]. stack = [4].
- Pop 4. res = [1, 3, 2, 5, 4]. stack = [].

[ END ]
- Loop finishes. 
- res is currently [1, 3, 2, 5, 4] (Root -> Right -> Left).
- We return res[::-1], reversing the list to: [4, 5, 2, 3, 1] (Left -> Right -> Root).

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the total number of nodes. We visit every node 
  exactly once to build the list, and reversing a list of size $N$ at the end takes an 
  additional $O(N)$ time. $O(2N)$ simplifies to $O(N)$.
- Space Complexity: $O(N)$ to store the final result array. The stack itself takes $O(H)$ 
  memory where $H$ is the height of the tree (scaling up to $O(N)$ in the worst-case skewed tree).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        # Base case: empty tree returns an empty list
        if not root:
            return []
        
        res = []
        
        # Initialize the stack with the root node
        stack = [root]

        # Standard iterative traversal loop
        while stack:
            # Pop the top node off the stack and immediately process it
            curr = stack.pop()
            res.append(curr.val)

            # Push LEFT child first, so it ends up BELOW the right child.
            if curr.left:
                stack.append(curr.left)
                
            # Push RIGHT child second, so it ends up ON TOP and gets popped first.
            if curr.right:
                stack.append(curr.right)
        
        # We built [Root, Right, Left]. Reverse it to get [Left, Right, Root].
        return res[::-1]
