class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        max_l = -1

        for i in range(len(s)):
            #checking as odd palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if max_l < right - left + 1:
                    result = s[left : right + 1]
                    max_l = right - left + 1
                left -= 1
                right += 1
            
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if max_l < right - left + 1:
                    result = s[left : right + 1]
                    max_l = right - left + 1
                left -= 1
                right += 1

        return result
