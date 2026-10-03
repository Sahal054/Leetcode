"""
199. Binary Tree Right Side View (Level Order / BFS)

--- The Core Intuition ---
1. The Perspective: Imagine standing physically on the right side of the tree and 
   looking left. You will only see the rightmost node of every single horizontal level. 
   If a right child is missing, you might see a left child peeking out from behind it!
2. Level-by-Level Navigation: Because we need exactly one node per horizontal slice, 
   a Breadth-First Search (BFS) using a Queue is the ideal approach.
3. Catching the Last Node: Just like in the previous BFS problems, we take a snapshot 
   of the queue size (`lenq`) to process one row at a time. As we loop through the row, 
   the very last node we pop (`i == lenq - 1`) is guaranteed to be the rightmost node 
   of that specific level. We grab its value and ignore the rest!
4. The Deque Upgrade: You perfectly implemented `collections.deque` and `popleft()` 
   here! This fixes the $O(N)$ time penalty of `pop(0)` and ensures your queue operations 
   are strictly $O(1)$.

--- Visual Traversal Walkthrough ---

Example: 
      1            <--- View: 1
    /   \
   2     3         <--- View: 3
    \     
     5             <--- View: 5 (Notice how the left branch peeks through!)

[ INITIAL SETUP ]
- q = deque([Node(1)])
- res = []

[ LEVEL 1 ]
- lenq = 1
- i = 0: Pop 1. 
  - i == 0 (which is lenq - 1). It's the rightmost! res.append(1).
  - Add children: q = [Node(2), Node(3)]

[ LEVEL 2 ]
- lenq = 2
- i = 0: Pop 2. 
  - i != 1. (Not the rightmost, skip appending).
  - Add children: q = [Node(5)]
- i = 1: Pop 3.
  - i == 1 (lenq - 1). It's the rightmost! res.append(3).
  - No children to add.
  - q = [Node(5)]

[ LEVEL 3 ]
- lenq = 1
- i = 0: Pop 5.
  - i == 0 (lenq - 1). It's the rightmost! res.append(5).
  - No children to add.

[ END ]
- Queue is empty. 
- Return [1, 3, 5].

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes. We visit every single node 
  exactly once. Thanks to `deque.popleft()`, popping from the front is truly $O(1)$, 
  making the whole traversal strictly linear in time.
- Space Complexity: $O(N)$ because the queue holds at most one entire level of the tree 
  at a time. In a balanced binary tree, the largest level (the bottom one) holds roughly 
  half of all the nodes ($N/2$).
"""

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # Base case: empty tree
        if not root:
            return []
        
        # Use deque for O(1) pops from the left
        q = collections.deque([root])
        res = []

        while q:
            # Snapshot the exact number of nodes in the current horizontal level
            lenq = len(q)

            for i in range(lenq):
                node = q.popleft()

                # If this is the absolute last node in the current level's loop,
                # it is the rightmost node. Add it to our results!
                if i == lenq - 1:
                    res.append(node.val)

                # Queue up the next level's children from left to right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
