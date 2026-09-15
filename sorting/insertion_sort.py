class Solution:
    def insertionSort(self, arr):
        # code here
        
        n = len(arr)
        i = 1
        
        while i < n:
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j]>temp:

                arr[j+1] = arr[j]   
                #now arr[j] is conceptually empty   
                j -= 1 
                    #moved j one step back
            arr[j+1] = temp
            i += 1
            
        return arr