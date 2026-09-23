class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r = len(matrix)
        c = len(matrix[0])

        new_matrix  = []

        for i in range(r):
            row = []
            for j in range(c):
                row.append(0)
            new_matrix.append(row)


        for row in range(r):
            for column in range(c):
                new_matrix[column][c-1-row] = matrix[row][column]
        
        for row in range(r):
            for column in range(c):
                matrix[row][column] = new_matrix[row][column]
