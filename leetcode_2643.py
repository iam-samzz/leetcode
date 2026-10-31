class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])

        result = None
        max_sum = -1
        for i in range(m):
            row_sum = sum(mat[i])
            if row_sum > max_sum:
                max_sum = row_sum
                result = [i , row_sum]
        return result
                
        