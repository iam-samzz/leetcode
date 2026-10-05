class Solution:
    def lowerBound(self, arr, target):
        # code here
        
        n = len(arr)
        low = 0
        high = n-1
        
        lower_index = n + 1 ##just for a higher value
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if arr[mid] >= target:
                lower_index = min(mid,lower_index)
                high = mid - 1
            else:
                #lower than target
                low = mid + 1
        
        if lower_index == n+1:
            return len(arr)
            
        return lower_index