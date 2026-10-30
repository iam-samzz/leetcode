class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        

        low = 0
        high = len(mat[0]) - 1

        

        while low <= high:


            mid = (low + high ) // 2
            
            # indexs maximum element in the mid column
            # M : Tuple
            M = self.findMaxIndex(mat, mid, len(mat))

            # value of mid element
            M_value = mat[M[0]][M[1]]

            # left element of M
            left = -1 if M[1] - 1 < 0 else mat[M[0]][M[1] - 1]

            #right element of M
            right = -1 if M[1] + 1 >= len(mat[0]) else mat[M[0]][M[1] + 1]

            if M_value > left and M_value > right:
                return list(M)
            elif M_value < right:
                # go to right side of the mountains, since at least one peak mountain will be there in the right side of the forest
                low = mid + 1
            elif M_value < left:
                # if left value is greater than the Maximum mid value
                # go to left side of the mountains, since at least one peak mountain will be there in the left side of the forest.
                high = mid - 1


            

            
    def findMaxIndex(self, mat, col, total_rows_count):
        r = 0
        max_index = None
        max_element = -1
        while r < total_rows_count:

            if mat[r][col] > max_element:
                max_element = mat[r][col]
                max_index = (r, col)
            r += 1
        return max_index
        
        