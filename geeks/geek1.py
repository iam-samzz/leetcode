'''Smallest window containing 0, 1 and 2'''

class Solution:
    def smallestSubstring(self, s):
        # code here
        
        n =len(s)
        
        left = 0
        
        #window state
        win = {}
        
        #result state
        min_len = float('inf')
        
        
        for right in range(n):
            if  s[right] not in win:
                win[s[right]] = 1
            else:
                win[s[right]] += 1
            
                #valid condition
            while (win.get('0')) and (win.get('1')) and (win.get('2')):
    
                min_len = min(min_len,right-left+1)
            
                win[s[left]] -= 1
                if win[s[left]] == 0:
                    del win[s[left]]
            
                left += 1
        if min_len == float('inf'):
            return -1
        return min_len