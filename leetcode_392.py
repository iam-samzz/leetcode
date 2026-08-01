class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        def function(s,t):
            ls = list(s)
            lt = list(t)

            p1 = 0

            founded = 0
            for p2 in range(0,len(lt)):
                if founded == len(s):
                    break
                if lt[p2] == ls[p1]:
                    founded += 1
                    p1 += 1
                
            if founded == len(ls):
                return True
            return False
        return function(s,t)
                
                    
