"""
Breadth-First Search (BFS) on a Binary Search Tree

BFS visits every node on a level before going to a lower level. We use a 
Queue (First-In-First-Out) to keep track of the nodes we need to visit next.

Based on the insertions (47, 21, 76, 18, 27, 52, 82), our tree looks like this:

Example Tree:
           47
         /    \
       21      76
      /  \    /  \
    18   27  52   82

Step-by-step execution:
(Note: The queue stores actual Node objects, but we use their values below for clarity)

Initialization:
queue = [47]
results = []

--- Iteration 1 ---
- Pop the front of the queue: current_node = 47, queue = []
- Add 47 to results: results = [47]
- 47 has a left child (21), add to queue: queue = [21]
- 47 has a right child (76), add to queue: queue = [21, 76]

--- Iteration 2 ---
- Pop the front: current_node = 21, queue = [76]
- Add 21 to results: results = [47, 21]
- 21 has a left child (18), add to queue: queue = [76, 18]
- 21 has a right child (27), add to queue: queue = [76, 18, 27]

--- Iteration 3 ---
- Pop the front: current_node = 76, queue = [18, 27]
- Add 76 to results: results = [47, 21, 76]
- 76 has a left child (52), add to queue: queue = [18, 27, 52]
- 76 has a right child (82), add to queue: queue = [18, 27, 52, 82]

--- Iteration 4 ---
- Pop the front: current_node = 18, queue = [27, 52, 82]
- Add 18 to results: results = [47, 21, 76, 18]
- 18 has no children. queue remains: [27, 52, 82]

--- Iteration 5 ---
- Pop the front: current_node = 27, queue = [52, 82]
- Add 27 to results: results = [47, 21, 76, 18, 27]
- 27 has no children. queue remains: [52, 82]

--- Iteration 6 ---
- Pop the front: current_node = 52, queue = [82]
- Add 52 to results: results = [47, 21, 76, 18, 27, 52]
- 52 has no children. queue remains: [82]

--- Iteration 7 ---
- Pop the front: current_node = 82, queue = []
- Add 82 to results: results = [47, 21, 76, 18, 27, 52, 82]
- 82 has no children. queue remains: []

Queue is now empty, while loop terminates.
Final output: [47, 21, 76, 18, 27, 52, 82]
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
   
    # YOU CAN ALSO WRITE BFS WITH A QUEUE INSTEAD OF LIST
    # (TECHNICALLY THIS IS A BETTER SOLUTION)
    #
    # def BFS(self):
    #     current_node = self.root
    #     queue = Queue()
    #     results = []
    #     queue.put(current_node)

    #     while not queue.empty():
    #         current_node = queue.get()
    #         results.append(current_node.value)
    #         if current_node.left is not None:
    #             queue.put(current_node.left)
    #         if current_node.right is not None:
    #             queue.put(current_node.right)
    #     return results
                
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results





my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())



"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]

 """





                



 
