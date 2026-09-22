class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        result = [arr[n-1]]
        
        leader = n-1
        current = n-2
        
        while current >= 0:
            if arr[current] >= arr[leader]:
                result.append(arr[current])
                leader = current
                current -= 1
            elif arr[current] < arr[leader]:
                current -= 1
        
        return result[::-1]
                