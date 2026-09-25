class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        n = numRows

        for i in range(1,n):
            temp = [0] + res[-1] + [0]
            x = []
            
            for j in range(len(res[-1]) + 1):

                x.append(temp[j]+temp[j + 1])
            
            res.append(x)
        return res
            

