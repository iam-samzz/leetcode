"""Given a string s, find the first non-repeating character in it and return
 its index. If it does not exist, return -1."""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        def find(s):
        
            #loading s into hashmap
            h = {}

            for i in s:
                if i not in h:
                    h[i] = 1
                else:
                    h[i] += 1
            
            for index,element in enumerate(s):
                if h[element] == 1:
                    return index
            
            return -1
        return find(s)
