class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        

        #using nested loops

        def func(word1,word2):
            if len(word2) > len(word1):
                return -1
            status = False
            for i in range(len(word1)):
                if word1[i] == word2[0] and len(word1[i:]) >= len(word2):
                    for j in range(len(word2)):
                        if word1[j + i] != word2[j]:
                            status = False
                            break
                        else:
                            status = True
                    if status == True:
                        return i
            if status == False:
                return -1
        
        return func(haystack,needle)
            