"""
141. Linked List Cycle (Floyd's Tortoise and Hare Algorithm)

The objective is to determine if a linked list contains a cycle. A cycle means 
that if you keep following the 'next' pointers, you will eventually loop back 
to a node you've already visited.

--- The Core Intuition: Two Runners on a Track ---
Imagine two runners on a circular race track:
1. A slow runner (Tortoise / 'slow' pointer) who moves 1 step at a time.
2. A fast runner (Hare / 'fast' pointer) who moves 2 steps at a time.

If the track is a straight line, the fast runner will hit the end of the line 
and the race stops (No Cycle).
If the track contains a loop, the fast runner will enter the loop first and 
begin circling. Eventually, because the fast runner gains 1 step of distance 
closer to the slow runner on every iteration, the fast runner is mathematically 
guaranteed to lap and meet the slow runner from behind!

[Image of linked list cycle detection algorithm]

--- Visual Linked List Layout ---

Example: head = [3, 2, 0, -4], pos = 1 (where -4 loops back to index 1, which is 2)

    Slow, Fast
       |
       V
     [ 3 ] ---> [ 2 ] ---> [ 0 ] ---> [ -4 ]
                  ^                     |
                  |_____________________|

Step-by-step Execution Trace:

Initialization:
slow = Node(3)
fast = Node(3)

--- Iteration 1 ---
- slow moves 1 step: slow = Node(2)
- fast moves 2 steps: fast = Node(0)
- Current state: slow != fast (2 != 0). Loop continues.

    Head          Slow                  Fast
     [ 3 ] ---> [ 2 ] ---> [ 0 ] ---> [ -4 ]
                  ^                     |
                  |_____________________|

--- Iteration 2 ---
- slow moves 1 step: slow = Node(0)
- fast moves 2 steps: fast passes -4 and wraps back to Node(2)
- Current state: slow != fast (0 != 2). Loop continues.

    Head          Fast                  Slow
     [ 3 ] ---> [ 2 ] ---> [ 0 ] ---> [ -4 ]
                  ^                     |
                  |_____________________|

--- Iteration 3 ---
- slow moves 1 step: slow = Node(-4)
- fast moves 2 steps: fast moves from 2 -> 0 -> Node(-4)
- Current state: slow == fast (-4 == -4)! 

                  Fast
                  Slow
                    |
                    V
     [ 3 ] ---> [ 2 ] ---> [ 0 ] ---> [ -4 ]
                  ^                     |
                  |_____________________|

- Collision detected! The code immediately returns True.

--- Complexity ---
- Time Complexity: O(n). If there is no cycle, the fast pointer reaches the end 
  in O(n) steps. If there is a cycle, the fast pointer will catch up to the slow 
  pointer in a number of steps proportional to the length of the list.
- Space Complexity: O(1) because we only use two pointer variables (slow, fast) 
  and don't allocate any extra memory.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize both pointers to start at the head node
        fast, slow = head, head

        # As long as the fast pointer hasn't hit a dead end (None)
        # We check both 'fast' and 'fast.next' to prevent an AttributeError
        while fast and fast.next:
            slow = slow.next          # Slow runner moves 1 step
            fast = fast.next.next     # Fast runner moves 2 steps
            
            # If they land on the exact same node object, a cycle exists
            if slow == fast:
                return True
                
        # If the loop terminates, the fast runner reached the end -> No cycle!
        return False
