class Solution:
    def longestSubarray(self, arr, k):  
        # code here
    
        left = 0
        right = 0
        n = len(arr)
        
        #window state
        win_sum = 0
        
        #return state
        max_l = 0
        
        
        while right < n:
            
            win_sum += arr[right]
            
            while win_sum > k:
                win_sum -= arr[left]
                left += 1
            if win_sum == k:
                max_l = max(max_l,right-left+1)
            
            right += 1
            
        return max_l