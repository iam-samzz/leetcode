class Solution:
    def insertionSort(self, arr):
        # code here
        
        n = len(arr)
        
        
        def func(arr,pos):
            if pos >= n:
                return
            i = pos - 1
            val = arr[pos]
            
            
            while i > -1:
                if arr[i] <= val:
                    break
                if arr[i] > val:
                    arr[i+1] = arr[i]
                i -= 1
            arr[i+1] = val
            
            func(arr,pos+1)
                
        func(arr,1)
        return arr