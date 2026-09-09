class Solution:
    def fib(self, n: int) -> int:
        
        def func(n):

            f = []

            for i in range(n+1):
                if i == 0 or i == 1:
                    f.append(i)
                else:
                    f.append(f[i-1] + f[i-2])
            return f[-1]
        return func(n)



            