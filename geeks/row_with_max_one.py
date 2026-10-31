class Solution:
    def rowWithMax1s(self, arr: list[list[int]]) -> int:
        # code here
        
        row_len = len(arr)
        col_len = len(arr[0])
        
        i = 0
        j = col_len - 1
        
        row_ans = -1
        
        while i < row_len and j >= 0:
            if arr[i][j] == 0:
                i += 1
            elif arr[i][j] == 1:
                row_ans = i
                j -= 1
        return row_ans