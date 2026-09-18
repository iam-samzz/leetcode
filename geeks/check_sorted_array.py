class Solution:
    def isSorted(self, arr):
        # code here
        i = 0 
        j = 1
        n = len(arr)
        
        while j < n:
            if arr[i] > arr[j]:
                return False
            i += 1
            j += 1
        return True