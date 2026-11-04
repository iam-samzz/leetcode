class Solution:
    def maxDepth(self, s: str) -> int:
        '''
            the maximum nesting depth represents the maximum number of open parentheses (`(`) active at any single point in time, not how many closing brackets appear consecutively
        '''
        
        p  = 0
        open_count = 0
        max_res = 0

        while p < len(s):

            if s[p] == '(':
                open_count += 1
                max_res = max(max_res , open_count)
                p += 1
            elif s[p] == ')':
                open_count -= 1
                p += 1
            else:
                p += 1
               
        return max_res
 