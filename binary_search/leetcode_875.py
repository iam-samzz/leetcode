import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        

        max_k = max(piles)

        low = 1 
        high = max_k

        min_k = max_k + 1

        while low <= high:
            mid = (low + high) // 2
            
            h_t = 0
            #finding total speed
            for i in range(len(piles)):

                hi = piles[i] / mid
                hi = math.ceil(hi)
                if hi <= 0:

                    h_t+= 1
                else:
                    h_t += hi
            
            if h_t > h:
                low = mid + 1
            elif h_t <= h:
                min_k = min(min_k , mid)
                high = mid - 1
        return min_k
                
