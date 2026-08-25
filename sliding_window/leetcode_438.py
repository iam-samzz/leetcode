class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def func(text, word):
            left = 0

            count = []
            win_hash = {}

            word_hash = {}
            for i in word:
                if i not in word_hash:
                    word_hash[i] = 1
                else:
                    word_hash[i] += 1

            for right in range(len(text)):

                if text[right] not in win_hash:
                    win_hash[text[right]] = 1
                else:
                    win_hash[text[right]] += 1

                if right - left + 1 == len(word):

                    #check if its anagram
                    if win_hash == word_hash:
                        count.append(right - len(word) + 1)

                    win_hash[text[left]] -= 1
                    if win_hash[text[left]] == 0:
                        del win_hash[text[left]]

                    left += 1
            return count
        return func(s,p)
