class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s)<=0:
            return 0
        total = (2**32 )
        MAX_INT = (total // 2) - 1
        MIN_INT =  (total // 2)
        p = 0
        
        
        
        if s[0] == '-':
            neg = True
            p += 1
        elif s[0] == "+":
            p += 1 
            neg = False
        else:
            neg = False
       
        result = 0
        while p < len(s):

            #give the integer value of s[p]
            current_digit = ord(s[p]) - ord('0')

            if current_digit >= 0 and current_digit <= 9:
                result = (result * 10) + current_digit
                if neg and result >= MIN_INT:
                    result = MIN_INT
                    break
                elif not neg and result >= MAX_INT:
                    result = MAX_INT
                    break
            else:
                break
            p+=1
        if neg: 
            return result*-1
        return result

