class Solution:
    def floorSqrt(self, n): 
        # code here
        if n == 1:
            return 1
        low = 1
        
        high = n // 2
        closer = None
        
        while low <= high:
            
            mid = (low + high) // 2
            
            sqr = mid**2
            
            if sqr == n:
                return mid
                
            elif sqr > n:
                high = mid - 1
                
            elif sqr < n:
                closer = mid    
                low = mid + 1
        
        return closer
        