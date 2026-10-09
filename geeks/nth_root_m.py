class Solution:
    def nthRoot(self, n, m):
       # code here
       
        low = 0
        high = m 
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if mid**n == m:
                return mid
            elif mid**n < m:
                low = mid + 1
            elif mid**n > mid:
                high = mid - 1
        return -1