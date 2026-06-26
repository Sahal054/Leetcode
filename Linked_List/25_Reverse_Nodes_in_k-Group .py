"""
25. Reverse Nodes in k-Group (In-Place Pointer Manipulation)

The objective is to reverse the nodes of a linked list k at a time and return its modified list. 
If the number of nodes is not a multiple of k, the remaining nodes at the end should be left 
exactly as they are.

Instead of extracting values or creating a new list (which takes extra memory), this solution 
reverses the nodes in place by carefully manipulating pointers, achieving a space complexity of O(1).

--- The Core Intuition ---
1. Dummy Node: A dummy node is placed before the head to handle cases where the head itself changes.
2. Group Tracking: `groupPrev` tracks the node immediately before the current k-group.
3. Finding Bounds: A helper function `getKth` identifies the last node of the current group (`kth`). 
   If it returns None, we have fewer than k nodes left, and we terminate.
4. In-Place Reversal: The standard linked-list reversal is used, but instead of initializing the 
   `prev` pointer to `None`, we initialize it to `groupNext` (the node right after the k-group). 
   This automatically links the tail of our reversed group to the rest of the list.
5. Reconnection: After reversal, the node that was previously right before the group (`groupPrev`) 
   is updated to point to the new head of the reversed group (`kth`). `groupPrev` is then advanced.

--- Step-by-Step Traversal Walkthrough ---

Example List: 1 -> 2 -> 3 -> 4 -> 5,  k = 2

[ INITIAL SETUP ]
Add a dummy node (0). 
groupPrev starts at 0.

Nodes:  [0] -> [1] -> [2] -> [3] -> [4] -> [5]
         ^      
     groupPrev 


[ ITERATION 1: Reversing Group 1, 2 ]
1. Find Bounds: 
   - kth = getKth(groupPrev, 2) -> Node 2
   - groupNext = kth.next -> Node 3

2. Reversal Loop (curr starts at 1, prev starts at 3):
   - curr (1) next points to prev (3).  [1 -> 3]
   - curr (2) next points to prev (1).  [2 -> 1 -> 3]
   (Loop ends because curr == groupNext)

   *Current State of Pointers:*
   Notice groupPrev (0) still points to 1! 
   [0] -> [1] <- [2]    [3] -> [4] -> [5]
           |_____________^

3. Group Connection:
   - temp = groupPrev.next (Node 1, which is the new tail of the reversed group)
   - groupPrev.next = kth (Node 0 now points to Node 2, straightening the list)
   - groupPrev = temp (groupPrev moves to Node 1, ready for the next group)

   *Result After Iteration 1:*
   [0] -> [2] -> [1] -> [3] -> [4] -> [5]
                  ^
              groupPrev


[ ITERATION 2: Reversing Group 3, 4 ]
1. Find Bounds:
   - kth = getKth(groupPrev, 2) -> Node 4
   - groupNext = kth.next -> Node 5

2. Reversal Loop (curr starts at 3, prev starts at 5):
   - curr (3) next points to prev (5).  [3 -> 5]
   - curr (4) next points to prev (3).  [4 -> 3 -> 5]

3. Group Connection:
   - temp = groupPrev.next (Node 3)
   - groupPrev.next = kth (Node 1 now points to Node 4)
   - groupPrev = temp (groupPrev moves to Node 3)

   *Result After Iteration 2:*
   [0] -> [2] -> [1] -> [4] -> [3] -> [5]
                                ^
                            groupPrev


[ ITERATION 3: Attempting Group 5 ]
1. Find Bounds:
   - kth = getKth(groupPrev, 2) -> Returns None (reached end of list).
2. Termination: 
   - `if not kth: break` triggers.

Final Return: dummy.next (Node 2)
Resulting List: 2 -> 1 -> 4 -> 3 -> 5

--- Complexity ---
- Time Complexity: O(n) because we traverse the list at most twice (once to find bounds, once to reverse).
- Space Complexity: O(1) as we only modify pointers in place without allocating new memory.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node simplifies edge cases where the head of the list changes
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find the kth node to determine the bounds of the current group
            kth = self.getKth(groupPrev, k)

            # If fewer than k nodes remain, we are done
            if not kth:
                break
            
            # Node immediately after our k-group
            groupNext = kth.next

            # Initialize pointers for the reversal
            # prev starts as groupNext to seamlessly connect the reversed group's tail
            prev, curr = kth.next, groupPrev.next
            
            # Standard linked list reversal strictly within the bounds of the group
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr 
                curr = temp 
            
            # Reconnect the reversed group to the node that preceded it
            # Save the node that will become the groupPrev for the NEXT iteration
            temp = groupPrev.next 
            # Point the previous block to the new head of this reversed block
            groupPrev.next = kth 
            # Advance groupPrev to the end of the newly reversed block
            groupPrev = temp 
            
        return dummy.next 


    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Helper function to traverse k nodes ahead.
        Returns the kth node, or None if there aren't enough nodes.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
