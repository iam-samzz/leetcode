class Solution:
    def bubbleSort(self,arr):
        # code here
        
        
        n = len(arr)
        def func(arr,n):
            
            if n == 1:
                return
            
            for j in range(n-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
            
            #larger element is at last
            func(arr,n-1)
        
            
            
        func(arr,n)
        return arr