"""
116. Populating Next Right Pointers in Each Node (Iterative / O(1) Space)

--- The Core Intuition ---
1. Exploiting the Linked List: Instead of using a Queue to group levels together, 
   we can just use the `.next` pointers we've ALREADY built! By the time you are 
   iterating through Level 2, its nodes are already connected like a linked list. 
   You can walk across Level 2 to wire up the children in Level 3.
2. The Two Connections: When standing at a parent node (`curr`), you have to make 
   two distinct wiring connections for the row below it:
   - Same Parent: The left child connects to the right child (`curr.left.next = curr.right`).
   - Different Parents (The Bridge): The right child must connect to the neighbor's 
     left child. We find the neighbor using the pointer we already built! 
     (`curr.right.next = curr.next.left`).
3. Level Navigation: 
   - `curr` traverses horizontally across the current level.
   - `nxt` acts as an anchor/bookmark. It simply remembers the very first node 
     of the row below, so when `curr` falls off the right edge of the tree, we 
     know exactly where to start the next row.

--- Visual Traversal Walkthrough ---

Example: 
      1
    /   \
   2     3
  / \   / \
 4   5 6   7

[ INITIAL SETUP ]
- curr = Node 1
- nxt = Node 2 (curr.left)

[ ROW 1 ]
- curr is 1:
  - Same Parent: 1.left.next = 1.right (Node 2 -> Node 3)
  - Different Parent: 1.next is None. Bridge step skipped.
  - curr moves to 1.next (None).
- curr is None. Drop down to next level:
  - curr = nxt (Node 2)
  - nxt = curr.left (Node 4)

[ ROW 2 ]
- curr is 2:
  - Same Parent: 2.left.next = 2.right (Node 4 -> Node 5)
  - Different Parent: 2.next is Node 3! So, 2.right.next = 3.left (Node 5 -> Node 6)
  - curr moves to 2.next (Node 3).
- curr is 3:
  - Same Parent: 3.left.next = 3.right (Node 6 -> Node 7)
  - Different Parent: 3.next is None. Bridge skipped.
  - curr moves to 3.next (None).
- curr is None. Drop down:
  - curr = nxt (Node 4)
  - nxt = curr.left (None, because 4 is a leaf)

[ ROW 3 (Leaves) ]
- The loop condition `while curr and nxt:` fails because `nxt` is None!
- Leaves don't have children to wire up, so we are completely done.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the number of nodes. We visit each parent node 
  exactly once to wire up its children.
- Space Complexity: $O(1)$. This is the most optimal solution. By using the `.next` 
  pointers to traverse horizontally, we completely eliminated the need for a Queue, 
  bringing the memory footprint down to strict constant time.
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Base case: empty tree
        if not root:
            return None
        
        # 'curr' walks across the current level.
        # 'nxt' points to the start of the next level down.
        curr, nxt = root, root.left

        # The loop stops when we reach the leaf level (nxt becomes None)
        while curr and nxt:
            
            # 1. Wire the left child to the right child (Same Parent)
            curr.left.next = curr.right

            # 2. Wire the right child to the neighbor's left child (Different Parent Bridge)
            if curr.next:
                curr.right.next = curr.next.left
            
            # Move horizontally to the next node in the current level
            curr = curr.next

            # If we reached the end of the current level...
            if not curr:
                # Drop down to the next level
                curr = nxt
                # Bookmark the start of the level below that
                nxt = curr.left
        
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
