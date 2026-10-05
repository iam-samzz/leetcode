class Solution:
    def upperBound(self, arr, target):
        # code here
        low = 0
        high = len(arr) - 1
        x = None
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= target:
                low = mid + 1
                
            elif arr[mid]  > target:
                high = mid - 1
        return low