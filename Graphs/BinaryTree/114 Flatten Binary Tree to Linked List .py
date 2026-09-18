"""
114. Flatten Binary Tree to Linked List (Recursive Bottom-Up / Tail Tracking)

--- The Core Intuition ---
1. The Preorder Problem: The problem asks us to flatten the tree in "preorder" 
   (Root -> Left -> Right). However, if we blindly start moving the left child 
   to the right side, we overwrite the original right child and lose it forever!
2. The Bottom-Up Solution: Instead of doing it top-down, we use Post-order traversal 
   (Left, Right, Root) to flatten the tree from the bottom up. By the time we are 
   standing at a node, we guarantee its left and right subtrees are already 
   perfectly flattened linked lists.
3. The Wiring Process: If a node has a flattened left subtree, we need to insert 
   that entire left list between the node and its right subtree. 
   - To do this, we must know the exact END (the tail) of the left list.
   - We connect `leftTail.right` to the original `root.right`.
   - We swing the entire left branch over to `root.right`.
   - We nullify `root.left`.
4. Returning the Tail: For this to work, our recursive `dfs` function must return 
   the *tail* (the very last node) of whatever subtree it just flattened. 
   The elegant Python line `rightTail or leftTail or root` picks the correct tail:
   - If there is a right branch, its tail is the absolute end of the list.
   - If there is no right branch, the left branch's tail is the end.
   - If it's a leaf node (no children), the node itself is the tail.

--- Visual Traversal Walkthrough ---

Example: 
      1
     / \
    2   5
   / \   \
  3   4   6

[ FLATTENING SUBTREE: Node 2 ]
- dfs(3) returns Node 3 as its tail.
- dfs(4) returns Node 4 as its tail.
- We are at Root 2. leftTail = 3, rightTail = 4.
- leftTail exists! Wire it up:
  - 3.right = 2.right (Node 4)
  - 2.right = 2.left (Node 3)
  - 2.left = None
- Subtree 2 is now flattened: 2 -> 3 -> 4
- Returns rightTail (Node 4) to the parent.

[ FLATTENING SUBTREE: Node 5 ]
- dfs(None) returns None for left.
- dfs(6) returns Node 6 as its tail.
- We are at Root 5. leftTail = None, rightTail = 6.
- No leftTail, so no wiring needed!
- Returns rightTail (Node 6) to the parent.

[ WIRING THE ROOT: Node 1 ]
- leftTail = Node 4 (the end of the 2->3->4 list).
- rightTail = Node 6 (the end of the 5->6 list).
- leftTail exists! Wire it up:
  - 4.right = 1.right (Node 5)
  - 1.right = 1.left (Node 2)
  - 1.left = None
- Returns rightTail (Node 6).

[ END ]
- The tree is fully flattened: 1 -> 2 -> 3 -> 4 -> 5 -> 6.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes. We visit every node 
  exactly once during the DFS traversal.
- Space Complexity: $O(H)$ where $H$ is the height of the tree, representing the 
  recursive call stack. In the worst case (a completely unbalanced tree), it's $O(N)$.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # dfs flattens the subtree and returns the TAIL node of that flattened list
        def dfs(root):
            if not root:
                return None
            
            # Recursively flatten the left and right subtrees
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            # If there was a left subtree, we must splice it in
            if leftTail:
                # 1. Connect the end of the left list to the start of the right list
                leftTail.right = root.right
                
                # 2. Move the whole left list over to the right child pointer
                root.right = root.left
                
                # 3. Clean up the left child pointer as required
                root.left = None
            
            # Return the tail of this newly merged list.
            # Python evaluates 'or' by returning the first truthy value it finds.
            last = rightTail or leftTail or root

            return last
        
        dfs(root)
