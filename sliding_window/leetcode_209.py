class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        def func(nums,target):
            left = 0
            right = 0

            minimum_length = None
            current_sum = 0

            for right in range(0,len(nums)):
                current_sum += nums[right]

                if current_sum >= target:

                    while current_sum >= target and left <= right:

                        l = right - left + 1
                        if minimum_length == None:
                            minimum_lenght = l
                        else:
                            minimum_length = min(l,minimum_length)

                        current_sum -= nums[left]

                        left += 1
            if minimum_length == None:
                return 0
            else:
                return minimum_length
        return  func(nums,target)
