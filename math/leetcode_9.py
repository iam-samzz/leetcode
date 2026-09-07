class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        value = str(x)

        left = 0
        right = len(value) - 1

        while left < right:
            if value[left] != value[right]:
                return False
            left += 1
            right -= 1
        return True