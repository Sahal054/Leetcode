class Solution(object):
    def rotate(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(r,col):
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]

        for r in range(row):
            matrix[r] =  matrix[r][::-1]   