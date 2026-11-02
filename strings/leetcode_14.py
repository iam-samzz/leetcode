class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        longest_prefix = -1
        #taking 1st word as reference
        for i in range(len(strs[0])):

            for j in range(1, len(strs)):
                if i +1 > len(strs[j]):
                    return strs[0][:longest_prefix + 1]
                if strs[j][i] != strs[0][i]:
                    # then correct:
                    return strs[0][:longest_prefix + 1]
                
            longest_prefix = i
        return strs[0][:longest_prefix + 1]