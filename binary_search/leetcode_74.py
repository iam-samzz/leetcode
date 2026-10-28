class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] == target  or matrix[mid][-1] == target:
                return True

            if target < matrix[mid][0]:

                if mid - 1 < top:
                    return False
                bottom = mid - 1

            elif target > matrix[mid][0] and target >matrix[mid][-1]:
                if mid + 1 > bottom:
                    return False
                top = mid + 1
            elif target > matrix[mid][0] and target < matrix[mid][-1]:
                # we got the row
                low = 0
                high = n - 1

                while low <= high:
                    mid2 = (low + high) // 2

                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] > target:
                        high = mid2 - 1
                    elif matrix[mid][mid2] < target:
                        low = mid2 + 1
                    
                return False
