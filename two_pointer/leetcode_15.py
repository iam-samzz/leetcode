class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        

        def func(nums):
            # a + b + c = 0
            nums.sort()
            result = []
            for i in range(len(nums)):
                

                if (nums[i] != nums[i-1] and i!=0) or i== 0:
                     
                    a = nums[i]

                    left = i+1
                    right = len(nums) - 1

                    #a + b + c = 0
                    #b + c = -(a)
                    # so our target is -(a)
                    target = -1 * a
                    while left < right:

                        if nums[left] + nums[right] > target:
                            right -= 1
                        elif nums[left] + nums[right] < target:
                            left += 1
                        else:
                            # when sum is = -(a)

                            result.append([a,nums[left],nums[right]])

                            left += 1
                            right -= 1
                            while nums[left] == nums[left-1] and left < right:
                                left += 1
                            while nums[right] == nums[right+1] and left < right:
                                right -= 1
            return result
        return func(nums)
        