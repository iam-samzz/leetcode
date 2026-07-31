class Solution:
    def reverseVowels(self, s: str) -> str:
        def func(s):

            # opposite pointer approach
            
            word = list(s)

            left = 0
            right = len(s) - 1
            vowels = {'a','e','i','o','u'}
            while left < right:
                if (word[left].lower() in vowels) and (word[right].lower() in vowels):

                    word[left],word[right] = word[right],word[left]
                    left += 1
                    right -= 1

                else:
                    if word[left].lower() not in vowels:
                        left += 1
                
                    if word[right].lower() not in vowels:
                        right -= 1

            return "".join(word)
        return func(s)
            
