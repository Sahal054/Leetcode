"""
380. Insert Delete GetRandom O(1)

--- The Core Intuition ---
1. The Problem with Arrays: An array (list) is perfect for `getRandom()` because you can 
   pick a random index in O(1) time. However, finding if an item exists takes O(N), and 
   deleting an item from the middle takes O(N) because all subsequent items must shift left.
2. The Problem with Hashmaps: A hashmap (dictionary) is perfect for O(1) inserts and O(1) 
   deletes. However, a hashmap has no indices! You cannot easily or efficiently pick a 
   random element from a hashmap.
3. The Solution (Combine Them): We use BOTH. The array holds the actual numbers so we can 
   pick randomly. The hashmap stores the exact index of each number in the array so we 
   can find them instantly.
4. The Magic Trick (Swap-with-Last Delete): To delete an item from the middle of the array 
   in O(1) time, we don't delete it directly. Instead, we take the VERY LAST item in the 
   array, copy it over the item we want to delete, and then pop the last item off the end 
   of the array. No shifting required! We then update the hashmap to point to the new location.

--- Visual Traversal Walkthrough ---

[ INITIAL SETUP ]
- numList = []
- hashmap = {}

[ INSERT: 10, 20, 30 ]
- Insert 10: numList = [10], hashmap = {10: 0}
- Insert 20: numList = [10, 20], hashmap = {10: 0, 20: 1}
- Insert 30: numList = [10, 20, 30], hashmap = {10: 0, 20: 1, 30: 2}

[ REMOVE: 20 ]
- Check hashmap: 20 exists at index `idx = 1`.
- Get the last value: `lastVal = 30`.
- Overwrite index 1 with 30: numList becomes [10, 30, 30].
- Pop the end: numList becomes [10, 30]. (Boom! 20 is gone in O(1) time).
- Update hashmap for the moved value (30): hashmap[30] = 1 (It used to be 2).
- Delete 20 from hashmap: hashmap = {10: 0, 30: 1}

[ GET RANDOM ]
- random.choice(numList) automatically picks an index between 0 and len(numList)-1. 
- Since the array is tightly packed with no gaps, this works flawlessly in O(1) time.

--- Complexity ---
- Time Complexity: $O(1)$ average time for `insert`, `remove`, and `getRandom`. 
  (Note: Hashmap operations are O(1) on average, though worst-case collisions could technically 
  be O(N), interviewers consider this O(1)).
- Space Complexity: $O(N)$ where $N$ is the number of elements. We store every element 
  twice: once in the array and once as a key in the hashmap.
"""

import random

class RandomizedSet:

    def __init__(self):
        # Maps the actual value to its current index in the array (val -> index)
        self.hashmap = {}
        # Stores the actual values to allow for O(1) random access
        self.numList = []
        
    def insert(self, val: int) -> bool:
        res = val not in self.hashmap

        # Only insert if it doesn't already exist
        if res:
            # Map the value to what will be its index (the current length of the array)
            self.hashmap[val] = len(self.numList)
            # Append it to the end of the array
            self.numList.append(val)
        
        return res
        
    def remove(self, val: int) -> bool:
        res = val in self.hashmap
        
        # Only remove if it actually exists
        if res:
            # 1. Find where the target value is located
            idx = self.hashmap[val]
            
            # 2. Identify the very last element in the array
            lastVal = self.numList[-1]
            
            # 3. Overwrite the target value with the last element
            self.numList[idx] = lastVal
            
            # 4. Pop the last element off the end (O(1) operation)
            self.numList.pop()
            
            # 5. Update the hashmap so the moved element points to its new index
            self.hashmap[lastVal] = idx
            
            # 6. Delete the target value from the hashmap entirely
            del self.hashmap[val]
        
        return res
        
    def getRandom(self) -> int:
        # random.choice picks a random element from a list in O(1) time
        return random.choice(self.numList)
