class Solution:
    def romanToInt(self, s: str) -> int:
        
        num = {
            'I' : 1,
            'V' : 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M':1000
        }
        p = 0

        su = 0
        while p < len(s):
            # current number
            n = num[s[p]]

            #next number
            next_number = 0 if p == len(s) - 1 else num[s[p + 1]]

            if n >= next_number:
                su += n
                p += 1
            elif n < next_number:
                p += 2
                su += (next_number - n)
        return su