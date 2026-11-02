class Solution:
    def reverseWords(self, s: str) -> str:
        l = len(s)
        f = 0
        b = l-1
        s = list(s)

        l = len(s)

        while len(s) > 0 and s[0] == ' ':
            s.pop(0)
        while len(s) > 0 and s[-1] == ' ':
            s.pop(-1)
        l = len(s)

        i = 0
        j = 0
        while j < l:
            if s[j] != ' ':
                s[i] = s[j]
                j += 1
                i += 1
            elif j <  l and s[j] == ' ' and s[j - 1] != ' ':
                s[i] = ' '
                j += 1
                i += 1
            elif j < l and s[j] == ' ' and s[j - 1] == ' ':
                j += 1
            

        while i < l:
            s.pop(-1)
            i+=1
    
        p = 0
        q = 0
        s = s[::-1]
        l = len(s)

        while q < l:

            #keeping q in end of the current word
            while q < l and  s[q] != ' ':
                q += 1
            
            #reverse the current word
            low = p
            high = q - 1
            while low < high :
                s[low] , s[high] = s[high] , s[low]
                low += 1
                high -= 1
            
            #keeping the  p and q in the starting of new word
            #if alreadt every word is ended, return

            while q < l and s[q] == ' ':
                q += 1
            p = q
        return "".join(s)