class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        count = 0
        n = len(nums)
        max_c = float('-inf')
        while left < n:
            if nums[left] == 1:
                count += 1
                max_c = max(count,max_c)
                left += 1
            else:
                count = 0
                left += 1
        if max_c == float('-inf'):
            return 0
        return max_c
