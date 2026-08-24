class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        def func(nums, k):
            max_1 = 0
            longest = 0
            left = 0
            right = 0


            while right < len(nums):
                if nums[right] != 1:
                    k -= 1

                if k < 0:
                    #stop right
                    while left <= right and  k < 0:
                        if nums[left] != 1:
                            k += 1
                        left += 1
                longest = max(longest , right - left + 1)
                right += 1
            return longest
        return func(nums, k)
