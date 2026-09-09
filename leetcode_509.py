class Solution:
    def fib(self, n: int) -> int:
        

        def fibo(n):
            
            if n == 0:
                return 0
            elif n == 1:
                return 1


            x = fibo(n-1) + fibo(n-2)

            return x

        return fibo(n)


    




            