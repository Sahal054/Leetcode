"""
129. Sum Root to Leaf Numbers (Recursive DFS)

--- The Core Intuition ---
1. Base-10 Shifting: As we travel down the tree, each new digit we encounter needs to 
   be appended to the end of our current number. Mathematically, we do this by taking 
   our current running total, multiplying it by 10 (which shifts all digits one place 
   to the left), and adding the new node's value. 
   (e.g., If we have 12, and we find a 3, (12 * 10) + 3 = 123).
2. The Leaf Node Check: We only return a completed number when we hit a strict leaf 
   node (a node with NO left child AND NO right child). 
3. The Accumulation: If a node is not a leaf, it passes its current sum down to both 
   its left and right children. The function then adds the results of those two branches 
   together and returns them up the tree.

--- Visual Traversal Walkthrough ---

Example: 
      4
    /   \
   9     0
  / \
 5   1

[ INITIAL CALL ]
- dfs(root=4, sum=0)
- sum = (0 * 10) + 4 = 4
- Not a leaf. Branch out: dfs(9, 4) + dfs(0, 4)

[ GOING DOWN THE LEFT BRANCH ]
- dfs(9, 4): 
  sum = (4 * 10) + 9 = 49
  Not a leaf. Branch out: dfs(5, 49) + dfs(1, 49)

- dfs(5, 49): 
  sum = (49 * 10) + 5 = 495. 
  Is it a leaf? YES (No left AND no right). Returns 495.

- dfs(1, 49): 
  sum = (49 * 10) + 1 = 491. 
  Is it a leaf? YES. Returns 491.

* Node 9 returns (495 + 491) = 986.

[ GOING DOWN THE RIGHT BRANCH ]
- dfs(0, 4): 
  sum = (4 * 10) + 0 = 40. 
  Is it a leaf? YES. Returns 40.

[ END ]
- Root node 4 returns (Left Branch 986 + Right Branch 40) = 1026.

--- Complexity ---
- Time Complexity: O(N) where N is the total number of nodes in the tree. We must 
  visit every single node exactly once to form all the numbers.
- Space Complexity: O(H) where H is the height of the tree. This is the memory used 
  by the recursive call stack. In the worst case (a completely unbalanced tree), 
  it degrades to O(N).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        
        def dfs(node, current_sum):
            # Base case: We hit a dead end (an empty child pointer)
            if not node:
                return 0
             
            # Shift the existing sum left by one base-10 digit, and add the new value
            current_sum = current_sum * 10 + node.val

            # STRICT LEAF CHECK: MUST be missing BOTH children
            if not node.left and not node.right:
                return current_sum
            
            # If not a leaf, gather the totals from both the left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # Start the traversal at the root with a starting sum of 0
        return dfs(root, 0)
