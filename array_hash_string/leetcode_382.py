class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        def func(ransom,mag):

            #Loading ransomnote on hash map
            r = {}
            for i in ransom:
                if i not in r:
                    r[i] = 1
                else:
                    r[i] = r[i] + 1
            m = {}
            for i in  mag:
                if i in m:
                    m[i] = m[i] + 1
                else:
                    m[i] = 1

            for key in r:
                if key not in m:
                    return False
                if not (m[key] >= r[key]):
                    return False

            return True

        return func(ransomNote,magazine)                
        