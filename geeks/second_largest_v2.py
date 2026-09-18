class Solution:
    def getSecondLargest(self, arr):
        max1 = None
        max2 = None

        for i in range(len(arr)):
            if max1 is None:
                max1 = arr[i]

            elif arr[i] > max1:
                max2 = max1
                max1 = arr[i]

            elif arr[i] != max1 and (max2 is None or arr[i] > max2):
                max2 = arr[i]

        if max2 is None:
            return -1

        return max2
        
                