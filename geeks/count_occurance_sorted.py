class Solution:
    def countFreq(self, arr, target):
        # code here
        
        n = len(arr)
        low = 0
        high = n - 1
        lower_bound_index = None
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] >= target:
                lower_bound_index = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
        if lower_bound_index == None or arr[lower_bound_index] != target:
            return 0
        else:
            count = 1
            
            while lower_bound_index < n:
                lower_bound_index += 1
                
                if lower_bound_index < n and arr[lower_bound_index] == target:
                    count += 1
                else:
                    break
            return count
            