class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:


        def func(code, k):

            n = len(code)
            res = [0] * n

            if k == 0:
                return res

            if k > 0:
                left = 1
                right = k
                s = sum(code[1:k+1])
                res[0] = s

                for i in range(n-1):

                    s = s - code[left]
                    left = (left +  1) % n

                    right = (right + 1) % n
                    s = s + code[right]

                    res[i + 1] = s
            elif k < 0:

                for i in range(0, n):
                    if i == 0:
                        right = (i - 1) % n
                        left = (i - abs(k)) % n
                        s = 0
                        for element in range(right,left-1,-1):
                            s = s + code[element % n]
                        res[0] = s
                        continue

                    s = s - code[left]
                    left = (left + 1) % n

                    right = (right + 1) % n
                    s = s + code[right]


                    res[i] = s
            return res
        return func(code,k)
