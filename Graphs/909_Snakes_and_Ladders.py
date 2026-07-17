"""
909. Snakes and Ladders (Graph & Breadth-First Search)

The objective is to find the minimum number of dice rolls required to reach the final 
square (N * N) on a Boustrophedon (zig-zag) numbered board. If you land on a square 
with a snake or ladder, you must immediately teleport to its destination.

This solution treats the board as a directed, unweighted graph where every dice roll 
(1 through 6) represents a directed edge. Since we need the *shortest path* in an 
unweighted graph, Breadth-First Search (BFS) is the optimal approach.

--- The Core Intuition ---
1. Board Orientation: The board numbers start at the bottom-left. By calling 
   `board.reverse()`, we flip the board upside down so that row index 0 corresponds 
   to the mathematical bottom row. This makes coordinate math much simpler.
2. 1D to 2D Mapping (`intToPos`): We need a way to translate a square number (e.g., 15) 
   into a 2D grid coordinate (r, c). 
   - `r` is simply `(square - 1) // length`.
   - `c` is `(square - 1) % length`. 
   - Because the board zig-zags, on odd rows (r % 2 != 0), the numbering goes right 
     to left. We adjust the column index accordingly: `c = length - 1 - c`.
3. BFS Traversal: We push the current square and the number of moves taken into a queue. 
   For each popped square, we simulate rolling a 6-sided die (adding 1 through 6).
4. Snakes and Ladders: If the destination square has a value other than -1, it's a 
   snake or ladder! The player's actual next square becomes that value.
5. Cycle Prevention: We use a `visit` set to record squares we've already reached. 
   Because BFS explores radially layer by layer, the first time we reach a square 
   is guaranteed to be the fastest way there.

--- Visual Traversal Walkthrough ---

Example 2x2 Board: 
Original:
  [ -1, -1 ]  <- Squares 4, 3
  [ -1,  4 ]  <- Squares 1, 2 (Notice the ladder at square 2 going to 4)

After `board.reverse()`:
Row 1: [ -1, -1 ]
Row 0: [ -1,  4 ]

[ INITIAL SETUP ]
length = 2. Target square = length * length = 4.
queue = [(1, 0)]   |   visit = set()

[ ITERATION 1: Popped (1, 0) ]
Square = 1, Moves = 0.

Roll the die (i from 1 to 6):
- Roll 1: nextSquare = 1 + 1 = 2
  - intToPos(2): r = 0, c = 1.
  - board[0][1] is 4! (Ladder found)
  - nextSquare teleports to 4.
  - nextSquare (4) == Target (4)!
  - Return moves + 1 (0 + 1 = 1).

Final Return: 1 roll is needed.

*What if it was a bigger board without an immediate win?* 
The algorithm would check all valid rolls (up to 6), resolve any snakes/ladders, 
check if they lead to the end, and if not, add them to the queue and `visit` set. 
The BFS structure guarantees that the first path to reach `N * N` is the shortest.

--- Complexity ---
- Time Complexity: O(N^2) where N is the length of the board. In the worst case, 
  we visit every square on the board exactly once.
- Space Complexity: O(N^2) to store the BFS queue and the `visit` set, which could 
  contain every square in the worst-case scenario.
"""

from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)

        # Reverse the board so that row 0 represents the bottom of the board
        board.reverse()
        
        def intToPos(square):
            """
            Helper function to convert a 1D square number (1 to N^2) 
            into 2D grid coordinates (row, col).
            """
            # Subtract 1 for zero-indexed math
            r = (square - 1) // length
            c = (square - 1) % length

            # If the row is odd, the board numbers go right-to-left
            if r % 2:
                c = length - 1 - c
            return [r, c]
        
        # Queue stores pairs of [current_square, moves_taken]
        queue = deque()
        queue.append([1, 0])
        visit = set()

        while queue:
            square, moves = queue.popleft()

            # Simulate rolling a 6-sided die
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                
                # If there's a snake or ladder, teleport to its destination
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                
                # If we've reached or exceeded the final square, we are done
                if nextSquare == length * length:
                    return moves + 1

                # If this is the first time we've reached this square, queue it
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    queue.append([nextSquare, moves + 1])
                    
        # If the queue empties and we never reached the end, it's impossible
        return -1
