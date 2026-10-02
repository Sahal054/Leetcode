
"""
117. Populating Next Right Pointers in Each Node II (Iterative Dummy Node / O(1) Space)

--- The Core Intuition ---
1. The Imperfect Tree Problem: In a perfect binary tree, we could confidently say 
   `curr.left.next = curr.right`. But in an imperfect tree, nodes might be missing 
   children, or there might be massive gaps between subtrees. The previous logic 
   completely shatters here.
2. The Linked List Builder: To safely navigate the gaps, we treat the level exactly 
   one step below us as a brand new, empty linked list. We create a `dummy` node to 
   act as the anchor for this next level, and a `tail` pointer to physically string 
   the children together.
3. The Horizontal Sweep: We use `curr` to walk horizontally across our current level 
   (which is already fully connected). Every time `curr` looks down and sees a valid 
   left or right child, it tells the `tail` pointer to grab it and attach it to our 
   growing linked list. 
4. Dropping Down: When `curr` reaches the end of the current row (`curr == None`), 
   the row below is fully built and connected! We simply set `curr = dummy.next` to 
   drop down to the very first node of that newly built row, and start the process over.

--- Visual Traversal Walkthrough ---

Example (Imperfect Tree): 
      1
     / \
    2   3
   /     \
  4       5

[ INITIAL SETUP ]
- curr = Node 1

[ ROW 1 ]
- Create dummy(0), tail = dummy.
- curr is 1:
  - Has left child (2): tail.next = 2, tail moves to 2.
  - Has right child (3): tail.next = 3, tail moves to 3.
  - curr moves to 1.next (None).
- Inner loop ends.
- Drop down: curr = dummy.next (Node 2).

[ ROW 2 ]
- Create NEW dummy(0), tail = dummy.
- curr is 2:
  - Has left child (4): tail.next = 4, tail moves to 4.
  - No right child.
  - curr moves to 2.next (Node 3).
- curr is 3:
  - No left child.
  - Has right child (5): tail.next = 5, tail moves to 5. 
    *(Notice how node 4 is perfectly connected to node 5, jumping the gap!)*
  - curr moves to 3.next (None).
- Inner loop ends.
- Drop down: curr = dummy.next (Node 4).

[ ROW 3 (Leaves) ]
- Create NEW dummy(0), tail = dummy.
- curr is 4: No children. curr moves to 4.next (Node 5).
- curr is 5: No children. curr moves to 5.next (None).
- Inner loop ends. 
- Drop down: curr = dummy.next (None, because tail never moved!).

[ END ]
- Outer loop breaks because curr is None.
- Return root.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes in the tree. We visit each 
  node essentially once when it is a child being wired up, and once when it is a parent 
  sweeping across the row.
- Space Complexity: $O(1)$. By using a lightweight dummy node and tail pointer, we 
  built the connections on the fly, completely avoiding the need for a memory-heavy Queue.
"""

# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Base case
        if not root:
            return None
        
        # curr walks horizontally across the level we are currently standing on
        curr = root

        while curr:
            # Create a dummy node to anchor the start of the next level down
            dummy = Node(0)
            
            # Tail will be used to string together the children of the current level
            tail = dummy
            
            # Sweep across the current level
            while curr: 
                # If a left child exists, append it to our next-level linked list
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                # If a right child exists, append it to our next-level linked list
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                # Move to the next neighbor in the current level
                curr = curr.next
        
            # Once we finish sweeping the current level, drop down to the level we just built.
            # dummy.next holds the very first node of that newly connected level.
            curr = dummy.next
    
        return root


"""
116. Populating Next Right Pointers in Each Node (Level Order / BFS)

--- The Core Intuition ---
1. Breadth-First Search (BFS): Because we want to connect nodes horizontally (left to right), 
   a level-order traversal using a Queue is the perfect approach. We process the tree 
   one full horizontal row at a time.
2. The Snapshot Technique: By checking `qlen = len(q)` at the start of the `while` loop, 
   we take a "snapshot" of exactly how many nodes are in the current row. The inner `for` 
   loop ensures we only process that exact number of nodes, preventing us from accidentally 
   processing the children we are adding for the next row.
3. Looking Ahead in the Queue: As we iterate through the row, the node we just popped 
   needs to point to its right neighbor. Where is its right neighbor? It's sitting at 
   the very front of the queue! We just peek at `q[0]` and point our node to it.
4. The Last Node Exception: The very last node in a row doesn't have a right neighbor 
   (it should point to `None`, which is its default state). We prevent it from linking 
   by checking `if i < qlen - 1`.

--- Visual Traversal Walkthrough ---

Example: 
      1
    /   \
   2     3
  / \   / \
 4   5 6   7

[ INITIAL SETUP ]
- q = [Node(1)]

[ LEVEL 1 ]
- qlen = 1.
- i=0 (Node 1): Pop 1. q is now []. 
  Is i < 0? No. (Doesn't link).
  Add children: q = [Node(2), Node(3)]

[ LEVEL 2 ]
- qlen = 2.
- i=0 (Node 2): Pop 2. q is now [Node(3)].
  Is i < 1? YES. Set Node(2).next = q[0] (which is Node 3).
  Add children: q = [Node(3), Node(4), Node(5)]
- i=1 (Node 3): Pop 3. q is now [Node(4), Node(5)].
  Is i < 1? No. (Doesn't link).
  Add children: q = [Node(4), Node(5), Node(6), Node(7)]

[ LEVEL 3 (Leaves) ]
- qlen = 4.
- i=0 (Node 4): Pop 4. q is [5, 6, 7]. i < 3? YES. Node(4).next = Node(5).
- i=1 (Node 5): Pop 5. q is [6, 7].    i < 3? YES. Node(5).next = Node(6).
- i=2 (Node 6): Pop 6. q is [7].       i < 3? YES. Node(6).next = Node(7).
- i=3 (Node 7): Pop 7. q is [].        i < 3? No. (Doesn't link).
- No children to add.

[ END ]
- Queue is empty. Return root.

--- Complexity ---
- Time Complexity: Logically, this is $O(N)$ because we visit every node once. 
  **However, Python specific warning:** You used a standard list for your queue and `pop(0)`. 
  In Python, `pop(0)` is an $O(N)$ operation because it forces every other element in the 
  list to shift left. This makes your current implementation $O(N^2)$ in time! To fix this 
  and get true $O(N)$ time, you should `import collections` and use `q = collections.deque()` 
  with `q.popleft()`.
- Space Complexity: $O(N)$. The queue holds an entire level of the tree at once. In a 
  perfect binary tree, the very bottom level contains exactly half of all the nodes ($N/2$). 
  Therefore, the memory scales linearly with the size of the tree.
"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Base case: empty tree
        if not root:
            return None
        
        # Initialize the queue for Breadth-First Search
        q = []
        q.append(root)

        # Process the tree level by level
        while q:
            # Snapshot the number of nodes currently in this level
            qlen = len(q)

            # Iterate through exactly the nodes in the current level
            for i in range(qlen):
                # Pop the first node from the queue
                node = q.pop(0)

                # If this is NOT the last node in the row, point its 'next' 
                # to the new front of the queue (its right neighbor)
                if i < qlen - 1:
                    node.next = q[0]
                
                # Enqueue the children for the next level's processing
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return root
