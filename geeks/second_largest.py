class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        max1 = None
        max_i = None
        for i in range(n):
            if max1== None:
                max1 = arr[i]
                max_i = i
                
            else:
                if max1 < arr[i]:
                    max1 = arr[i]
                    max_i = i
        max2 = None
        for i in range(n):
            if  i != max_i:
                if max2 == None:
                    if arr[i] != max1:
                        max2 = arr[i]
                else:
                    if arr[i] > max2 and arr[i]!=max1:
                        max2 = arr[i]
                
        if max2 == None:
            return -1
        return max2
            
        
                
                    
                
                