class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        

        row_len = len(mat)
        col_len = len(mat[0])

        i = 0
        j = 0

        while True:
            index_hash = {}
            # find all elements in all 8 sides
            a = -1 if j - 1 < 0 or i - 1 < 0 else mat[i][j - 1]
            index_hash[a] = (i , j-1)
            b =  -1 if i - 1 < 0 else mat[i-1][j]
            index_hash[b] = (i-1,j)
            c = -1 if j + 1 >= col_len or i - 1 < 0 else mat[i-1][j+1]
            index_hash[c] = (i-1 , j+1)


            d = -1 if j- 1<0 else mat[i][j-1]
            index_hash[d] = (i,j-1) 
            e = -1 if j + 1 >= col_len else mat[i][j+1]
            index_hash[e] = (i , j+1)

            f = -1 if i + 1>= row_len or j - 1 < 0 else mat[i + 1][j - 1]
            index_hash[f] = (i+1, j-1)
            g = -1 if i + 1>= row_len else mat[i + 1][j]
            index_hash[g] = (i+1 , j)
            h = -1 if i  + 1 >= row_len or j + 1>= col_len else mat[i+1][j + 1]
            index_hash[h] = (i+1 , j+1)

    

            sides = [ a , b , c , d ,e, f, g , h ]
            maxi = max(sides)
            if maxi < mat[i][j]:
                return [i , j]
            else:
                # finding the index of maxi

                i = index_hash[maxi][0]
                j = index_hash[maxi][1]
