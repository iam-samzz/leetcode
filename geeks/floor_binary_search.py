class Solution:
    def findFloor(self, arr, x):
        # code here
        
        
        low = 0
        high = len(arr) - 1
        ans = None
        
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= x:
                ans = mid
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
                
        if ans != None:
            return ans
        return -1