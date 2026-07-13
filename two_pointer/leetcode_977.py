class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        def merge(arr1,arr2):
            p1 = 0
            p2 = 0
            result = []

            #basically we are using 2 pointer method, which is 2pointer on 2 sequence
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    result.append(arr1[p1])
                    p1 += 1
                elif arr2[p2] < arr1[p1]:
                    result.append(arr2[p2])
                    p2 += 1
                else:
                    result.append(arr1[p1])
                    p1 += 1

                    result.append(arr2[p2])
                    p2 += 1
            if p1 != len(arr1):
                for i in range(p1,len(arr1)):
                    result.append(arr1[i])
            if p2 != len(arr2):
                for i in range(p2,len(arr2)):
                    result.append(arr2[i])

            return result

        def sort(arr):
            
            if len(arr) <= 1:
                return arr
            middle_element = (len(arr) // 2) 
            left_sorted = sort(arr[:middle_element])
            right_sorted = sort(arr[middle_element:])

            return merge(left_sorted,right_sorted)


        def function(arr):
            for i in range(0,len(arr)):
                arr[i] = arr[i]**2
            
            #now the arrray is squared.
            #we lets implement sorting 

            return sort(arr)
            
        return function(nums)
