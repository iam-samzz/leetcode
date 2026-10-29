class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_len = len(matrix)
        col_len = len(matrix[0])

        i = 0
        j = col_len - 1

        while  i < row_len and j >= 0:
           
                if  matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    i += 1
                elif matrix[i][j] > target:
                    j -= 1

        return False
        