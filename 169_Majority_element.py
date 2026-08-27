from typing import Counter


class Solution(object):
    def majorityElement(self, nums):
        s = Counter(nums)

        for i, v in s.items():
            if v > len(nums)//2:
                return i 
class Solution(object):
    def majorityElement(self, nums):
        hashmap ={}


        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] =1   

        for i, v in hashmap.items():
            if v > len(nums)//2:
                return i 

# Time complexity = O(n)
#Space complexity =O(n)


"""
169. Majority Element (Boyer-Moore Voting Algorithm)

--- The Core Intuition ---
1. The Battlefield Analogy: Imagine the array as a battlefield. Each unique number 
   represents a different faction of soldiers. When two soldiers from DIFFERENT 
   factions meet, they mutually destroy each other. 
2. The Majority Guarantee: The problem guarantees that the majority element appears 
   more than `n / 2` times. This means the majority faction has more soldiers than 
   ALL other factions combined. 
3. The Last Man Standing: Even if every single enemy soldier manages to perfectly 
   take down one of the majority soldiers, the majority faction will STILL have at 
   least one soldier left standing at the end.
4. The Implementation: We maintain a `res` (our current candidate) and a `count` 
   (their health or number of reinforcements). 
   - If `count` is 0, the previous candidate's army has been wiped out. The very 
     next number takes the throne as the new candidate (`res = i`).
   - If the next number matches our candidate, they get a reinforcement (`count += 1`).
   - If the next number is an enemy, they mutually destroy one another (`count -= 1`).

--- Visual Traversal Walkthrough ---

Example: nums = [2, 2, 1, 1, 1, 2, 2]

[ INITIAL SETUP ]
- res = 0, count = 0

[ i = 2 ]
- count == 0. New candidate! res = 2.
- 2 == res, so count += 1. (count = 1)

[ i = 2 ]
- 2 == res, so count += 1. (count = 2)

[ i = 1 ]
- 1 != res, enemy encountered! count -= 1. (count = 1)

[ i = 1 ]
- 1 != res, enemy encountered! count -= 1. (count = 0)
* The '2' faction has been temporarily wiped out.

[ i = 1 ]
- count == 0. New candidate! res = 1.
- 1 == res, so count += 1. (count = 1)

[ i = 2 ]
- 2 != res, enemy encountered! count -= 1. (count = 0)
* The '1' faction has been wiped out.

[ i = 2 ]
- count == 0. New candidate! res = 2.
- 2 == res, so count += 1. (count = 1)

[ END ]
- Loop finishes. The last man standing is `res` (2). Return 2.

--- Complexity ---
- Time Complexity: $O(N)$ where $N$ is the length of `nums`. We do a single pass 
  through the array.
- Space Complexity: $O(1)$. We only track two variables (`count` and `res`), requiring 
  zero scaling memory regardless of how massive the array gets. This makes it far 
  superior to using a Hashmap to count frequencies.
"""

class Solution(object):
    def majorityElement(self, nums):
        count, res = 0, 0

        for i in nums:
            # If the current candidate's count drops to 0, pick a new candidate
            if count == 0:
                res = i

            # If the current number is our candidate, gain a vote. Else, lose a vote.
            count += (1 if i == res else -1)

        return res
    
