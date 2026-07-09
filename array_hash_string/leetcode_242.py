class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        def check_anagram(s,t):
            if len(s)!=len(t):
                return False
            
            #loading t in hash map
            thash = {}
            
            for t_element in t:
                if t_element not in thash:
                    thash[t_element] = 1
                else:
                    thash[t_element] = thash[t_element] + 1
            

            #loading s_element in shash
            shash = {}
            for i in s:
                if i not in shash:
                    shash[i] = 1
                else:
                    shash[i] = shash[i] + 1
            
            status = True
            for key in shash:
                if key in thash:
                    if shash[key] == thash[key]:
                        status = True
                        
                    else:
                        status = not status
                        break
                else:
                    status = False
                    break
            return status
                
        return check_anagram(s,t)


