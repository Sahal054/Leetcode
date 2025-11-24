class Solution(object):
    def setZeroes(self, matrix):
        ROWS,COLS = len(matrix),len(matrix[0])
        ROWZERO = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        ROWZERO = True

        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c] ==0 or matrix[r][0] == 0:
                    matrix[r][c] =0 
        if matrix[0][0] == 0:
            for r in range (ROWS):
                matrix[r][0] =0
        if ROWZERO:
            for c in range(COLS):
                matrix[0][c]  = 0
# - Time complexity: O(M*N)
# - Space complexity: O(1)


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zero_row = set()
        zero_col = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in range(row):
            for j in range(col):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0

# - Time complexity: O(M*N)
# - Space complexity: O(M+N)