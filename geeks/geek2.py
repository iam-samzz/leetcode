class Solution:
    def solve(self, n: int, k: int, geekNum: list[int]) -> int:
        # code here
        given_len = len(geekNum)
        
        for right in range(n):
            
            if given_len!=0:
                given_len -= 1
            else:
                s = 0
                x = right
                for i in range(k):
                    s += geekNum[right-1-i]
                    x -= 1
                geekNum.append(s)
        return geekNum[-1]