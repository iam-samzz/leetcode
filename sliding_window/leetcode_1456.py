class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        


        def func(s_list,k):
            # window size = k (eg: 3)
            VOWELS = {'a','e','i','o','u'}
            max_v = 0
            window_vowel_count = 0

            left = 0
            for i in range(left,k):
                if s_list[i] in VOWELS:
                    window_vowel_count += 1
            max_v = window_vowel_count

            for right in range(k-1,len(s_list)-1):
                
                if s_list[left] in VOWELS:
                    window_vowel_count -= 1
                left += 1

                right += 1

                if s_list[right] in VOWELS:
                    window_vowel_count += 1
                
                max_v = max(max_v,window_vowel_count)

            return max_v
        return func(s,k)
