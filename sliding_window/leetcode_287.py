class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def func(nums):
            h1 = {}
            for element in range(len(nums)):
                if nums[element] not in h1:
                    h1[nums[element]] = 1
                else:
                    h1[nums[element]] += 1

            for key in h1:
                if h1[key] > 1:
                    return key
            return None
        return func(nums)