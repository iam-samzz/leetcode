class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        h = {}
        for word in strs:
            word_list = list(word)
            word_list.sort()
            key = "".join(word_list)

            if key not in h:
                h[key] = [word]
            else:
                h[key].append(word)
        
        res = []
        for key in h:
            res.append(h[key])
        return res
