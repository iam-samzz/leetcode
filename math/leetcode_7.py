class Solution:
    def reverse(self, x: int) -> int:
        
        def func(num):

            if num == 0:
                return 0
            elif num < 0 :
                neg = True
                num = -1 * num
                x = num
            else:
                neg = False
                x = num
            r = 0
            
            digit = 0

            while x!=0:
                x = x // 10
                digit += 1
            digit -= 1
            while num != 0:
                r += (num % 10) * (10**digit)
                num = num // 10
                digit -= 1
            if neg == True:
                r = -1 * r
            if (r in range(0, 2** 31+1)) or (r in range(-1,-2**31-1,-1)):
                return r
            else:
                return 0
        return func(x)