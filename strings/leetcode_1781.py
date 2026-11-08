class Solution:
    def beautySum(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            h = {}
            mx = float('-inf')
            mn = float('inf')
            r = 0
            for j in range(i , len(s)):
                if s[j] not  in  h:
                    h[s[j]] = 1
                else:
                    h[s[j]] += 1

                mx = max(h.values())
                mn = min(h.values())

                r += (mx - mn)
            tot += r
        return tot

            
                