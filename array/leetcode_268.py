class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        r = set(nums)

        for i in range(n+1):
            if i not in r:
                return i