"""
146. LRU Cache (Hash Map + Doubly Linked List)

The objective is to design a data structure that follows the constraints of a 
Least Recently Used (LRU) cache. It must support `get` and `put` operations, 
both in O(1) average time complexity. When the cache reaches its capacity, it 
should invalidate (evict) the least recently used item before inserting a new one.

This solution combines two data structures:
1. A Hash Map (Dictionary) provides O(1) time access to the values via their keys.
2. A Doubly Linked List (DLL) maintains the usage history. It allows us to remove 
   and insert nodes in O(1) time because the Hash Map gives us direct pointers 
   to the nodes we need to move.

--- The Core Intuition ---
1. The Dummy Nodes: To avoid tedious edge cases (like inserting into an empty list 
   or deleting the last node), we use two dummy nodes: `left` and `right`.
   - `left` represents the Least Recently Used (LRU) boundary. The actual LRU node 
     is always `left.next`.
   - `right` represents the Most Recently Used (MRU) boundary. The actual MRU node 
     is always `right.prev`.
2. The `remove` Helper: Unlinks a node from its current position by pointing its 
   surrounding neighbors directly to each other.
3. The `insert` Helper: Always inserts a node directly before the `right` dummy node, 
   marking it as the Most Recently Used.
4. The `get` Operation: If the key exists, it has just been "used". We must `remove` 
   it from its current spot and `insert` it at the MRU end before returning its value.
5. The `put` Operation: If the key exists, remove the old node. Create a new node, 
   `insert` it at the MRU end, and update the hash map. If the capacity is exceeded, 
   we look at `left.next` (the LRU node), `remove` it from the list, and delete its 
   key from the hash map.

--- Visual Traversal Walkthrough ---

Example: capacity = 2
Operations: put(1, 1), put(2, 2), get(1), put(3, 3)

[ INITIAL SETUP ]
DLL:  [LEFT] <-> [RIGHT]
Map:  {}

[ OP 1: put(1, 1) ]
- Create Node(1). Insert at MRU (before RIGHT).
- DLL:  [LEFT] <-> [1] <-> [RIGHT]
- Map:  {1: Node(1)}

[ OP 2: put(2, 2) ]
- Create Node(2). Insert at MRU.
- DLL:  [LEFT] <-> [1] <-> [2] <-> [RIGHT]
- Map:  {1: Node(1), 2: Node(2)}
*(Capacity is 2. We are full, but not over capacity).*

[ OP 3: get(1) ]
- Key 1 exists in Map! 
- Action: remove Node(1) from current spot, insert at MRU.
- DLL:  [LEFT] <-> [2] <-> [1] <-> [RIGHT]
- Return: 1
*(Notice how Node 1 is now the most recently used, pushing Node 2 to the LRU spot)*

[ OP 4: put(3, 3) ]
- Create Node(3). Insert at MRU.
- DLL:  [LEFT] <-> [2] <-> [1] <-> [3] <-> [RIGHT]
- Map:  {1: Node(1), 2: Node(2), 3: Node(3)}
- Check Capacity: len(Map) is 3 > 2. We must evict!
- Identify LRU: left.next is Node(2).
- Action: remove Node(2) from DLL, delete key 2 from Map.
- DLL:  [LEFT] <-> [1] <-> [3] <-> [RIGHT]
- Map:  {1: Node(1), 3: Node(3)}

--- Complexity ---
- Time Complexity: O(1) for both `get` and `put`. Hash Map lookups/insertions are O(1), 
  and manipulating a Doubly Linked List is O(1) when you have a direct pointer to the node.
- Space Complexity: O(capacity) since the Hash Map and the Doubly Linked List will store 
  at most `capacity` number of nodes.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        # Pointers for the doubly linked list
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Hash map: key -> Node pointer
        self.cache = {}

        # Dummy nodes for boundaries
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        # Connect dummy nodes to each other initially
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        """Removes a node from anywhere in the doubly linked list."""
        prev = node.prev
        nxt = node.next
        
        # Point the neighbors at each other, isolating the current node
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """Inserts a node directly before the RIGHT dummy node (MRU position)."""
        prev = self.right.prev
        nxt = self.right

        # Connect the new node to its neighbors
        nxt.prev = node
        node.next = nxt

        # Connect the neighbors to the new node
        prev.next = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # If accessed, it becomes the most recently used. 
            # Move it to the MRU position by removing and re-inserting.
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
            
        return -1        

    def put(self, key: int, value: int) -> None:
        # If the key already exists, remove the old version to make way for the update
        if key in self.cache:
            self.remove(self.cache[key])
            
        # Create the new node, add to map, and insert at MRU position
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Check if we exceeded capacity
        if len(self.cache) > self.capacity:
            # The LRU node is always the one right after the LEFT dummy node
            lru = self.left.next
            
            # Remove from linked list and delete from hash map
            self.remove(lru)
            del self.cache[lru.key]
