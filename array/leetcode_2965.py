class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        # n value will be from 2 -> 50
        # so lets create a counting based method
        #counting star based method
        n = len(grid)
        count = [0]*((50**2) + 1)
        # every index is considered as number, 
        # in count i value will be from i = 0 to i = 50 (total 51 block of memory)
        
        a = None
        b = None

        for row in range(n):
            for column in range(n):
                current_element = grid[row][column]
                count[current_element] += 1

        #iterating count list for finding a and b
        for i in range(1,(n**2)+1):
            if count[i] == 2:
                a = i
            elif count[i] == 0:
                b = i
        return [a,b]
