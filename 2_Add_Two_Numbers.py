"""
2. Add Two Numbers (Linked List Elementary Math Simulation)

The objective is to add two numbers represented by two linked lists, where the digits 
are stored in REVERSE order (least significant digit first). We need to return the 
sum as a new linked list.

--- The Core Intuition: School Addition ---
This algorithm simply simulates traditional column-by-column addition from right to left.
Because the lists are already in reverse order, the head of the list is the ones column, 
the next node is the tens column, and so on. This actually makes our lives much easier!

We track three moving pieces at any given position:
1. v1: The value of the current node in list 1 (or 0 if list 1 runs out of digits).
2. v2: The value of the current node in list 2 (or 0 if list 2 runs out of digits).
3. carry: The extra digit passed to the next column when a column sum exceeds 9.

Formulas for each column calculation:
$$\text{val} = v_1 + v_2 + \text{carry}$$
$$\text{new carry} = \text{val} // 10$$
$$\text{node value} = \text{val} \% 10$$



--- Visual Linked List Layout ---

Example: l1 = [2, 4, 3] (represents 342) 
         l2 = [5, 6, 4] (represents 465)

    l1:  [ 2 ] ---> [ 4 ] ---> [ 3 ]
           +          +          +
    l2:  [ 5 ] ---> [ 6 ] ---> [ 4 ]
           |          |          |
           V          V          V
    res: [ 7 ] ---> [ 0 ] ---> [ 8 ]  (represents 807)

--- Step-by-Step Execution Trace ---

Initialization:
dummy = ListNode(0)
curr = dummy
carry = 0

--- Iteration 1 ---
- l1 is at [2], l2 is at [5] -> v1 = 2, v2 = 5
- val = 2 + 5 + 0 (carry) = 7
- carry = 7 // 10 = 0
- val = 7 % 10 = 7
- Create node(7): dummy -> [7]
- Move curr to [7]. Advance l1 to [4] and l2 to [6].

--- Iteration 2 ---
- l1 is at [4], l2 is at [6] -> v1 = 4, v2 = 6
- val = 4 + 6 + 0 (carry) = 10
- carry = 10 // 10 = 1  (We have a carry!)
- val = 10 % 10 = 0
- Create node(0): dummy -> [7] -> [0]
- Move curr to [0]. Advance l1 to [3] and l2 to [4].

--- Iteration 3 ---
- l1 is at [3], l2 is at [4] -> v1 = 3, v2 = 4
- val = 3 + 4 + 1 (carry) = 8
- carry = 8 // 10 = 0
- val = 8 % 10 = 8
- Create node(8): dummy -> [7] -> [0] -> [8]
- Move curr to [8]. l1 and l2 both advance to None.

The while loop ends because l1 is None, l2 is None, and carry is 0.
Final Result: dummy.next -> [7, 0, 8]

--- Complexity ---
- Time Complexity: O(max(M, N)) where M and N are the lengths of l1 and l2. 
  We iterate at most max(M, N) + 1 times.
- Space Complexity: O(max(M, N)) to allocate the new nodes for the output linked list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # A placeholder node that stays at the start so we don't lose the head of our new list
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        # Loop continues if there are digits left in l1, l2, OR an outstanding carry digit
        while l1 or l2 or carry:
            # Extract values dynamically, defaulting to 0 if one list finishes early
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate total value for the current column
            val = v1 + v2 + carry
            carry = val // 10   # Determine new carry (will be either 0 or 1)
            val = val % 10      # Determine single digit value to store in the node
            
            # Construct and link the new digit node
            curr.next = ListNode(val)
            curr = curr.next
            
            # Move both input pointers forward safely
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        # Return the actual head node, skipping the initial dummy node
        return dummy.next
