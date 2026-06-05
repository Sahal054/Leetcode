"""
206. Reverse Linked List (Iterative Three-Pointer Approach)

The objective is to reverse a singly-linked list in place. This means mutating 
the existing nodes so that their 'next' pointers directionally point backwards 
instead of forwards.

--- The Core Intuition: Flipping the Arrows ---
To reverse a linked list, we must change every node's 'next' pointer to point to 
its previous node. However, if we simply break the forward link immediately, 
we lose access to the remainder of the list! 

To prevent this, we use a three-pointer technique that acts like a rolling window:
1. prev: Tracks the node behind us (starts as None).
2. curr: Tracks the node we are currently modifying.
3. after: A temporary scout that remembers the rest of the list ahead of us 
          before we break the forward bridge.



--- Visual Pointer Manipulation ---

Original:      [1] ----> [2] ----> [3] ----> None
Reversed:     None <---- [1] <---- [2] <---- [3] (Returned as new head)

--- Step-by-Step Execution Trace ---

Example Input: head = [1, 2, 3]

Initialization:
prev = None
curr = Node(1)

--- Iteration 1 ---
- Save the forward path: after = curr.next  -> Node(2)
- Flip the pointer:     curr.next = prev   -> None   (Node 1 now points backwards to None)
- Slide prev forward:   prev = curr        -> Node(1)
- Slide curr forward:   curr = after       -> Node(2)

    None <--- [1]       [2] ---> [3] ---> None
               ^         ^
              prev      curr (after)

--- Iteration 2 ---
- Save the forward path: after = curr.next  -> Node(3)
- Flip the pointer:     curr.next = prev   -> Node(1)(Node 2 now points backwards to Node 1)
- Slide prev forward:   prev = curr        -> Node(2)
- Slide curr forward:   curr = after       -> Node(3)

    None <--- [1] <--- [2]       [3] ---> None
                        ^         ^
                       prev      curr (after)

--- Iteration 3 ---
- Save the forward path: after = curr.next  -> None
- Flip the pointer:     curr.next = prev   -> Node(2)(Node 3 now points backwards to Node 2)
- Slide prev forward:   prev = curr        -> Node(3)
- Slide curr forward:   curr = after       -> None

    None <--- [1] <--- [2] <--- [3]      None
                                 ^        ^
                                prev     curr (after)

The while loop terminates because curr is now None.
Final Result: prev points to Node(3), which links all the way back to Node(1).

--- Complexity ---
- Time Complexity: O(n) where n is the number of nodes in the linked list. 
  We visit each node exactly once.
- Space Complexity: O(1) because the reversal is performed completely in-place 
  by shifting pointers, using no extra data structures.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 'prev' starts as None because the old head will become the new tail
        prev, curr = None, head

        while curr:
            # 1. Stash the next node so we don't lose the rest of the list
            after = curr.next
            
            # 2. Reverse the link (point backwards)
            curr.next = prev 
            
            # 3. Step forward: 'prev' takes the place of 'curr'
            prev = curr
            
            # 4. Step forward: 'curr' moves to the node we stashed earlier
            curr = after
            
        # 'prev' is left standing on the very last node processed, the new head
        return prev
