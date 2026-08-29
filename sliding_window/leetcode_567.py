class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        left = 0 

        #s1 hash
        s1_hash = {}
        for i in s1:
            if i not in s1_hash:
                s1_hash[i] = 1
            else:
                s1_hash[i] += 1

        #window_state
        win_hash = {}
        k = len(s1)

        for right in range(n2):
            
            window_size = right - left + 1
            if s2[right] not in win_hash:
                win_hash[s2[right]] = 1
            else:
                win_hash[s2[right]] += 1
            
            if window_size == k:
                if win_hash == s1_hash:
                    return True

                if s2[left] in win_hash:
                    win_hash[s2[left]] -= 1
                    if win_hash[s2[left]] == 0:
                        del win_hash[s2[left]]
                left += 1
        return False
    


            
            
