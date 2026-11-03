class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False
        h1 = {}
        h2 = {}
        p1 = 0 # for t

        while p1 < lt:
            if t[p1] not in h1:
                h1[t[p1]] = s[p1]
            else:
                # see wherer that value and current equavalent s[i] is same
                #if same, then move on
                # if not same, then s is in different structure, and not isomorphic
                if h1[t[p1]] != s[p1]:
                    return False


            if s[p1] not in h2:
                h2[s[p1]] = t[p1]
            else:
                if h2[s[p1]] != t[p1]:
                    return False
    
            p1 += 1
        return True