class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # 0, 1, 2
        #dutch national flag algorithm

        def func(nums):
            low = 0
            mid = 0
            high = len(nums) - 1

            while mid <= high:
                if nums[mid] == 0: #i.e lowest value
                    #swap with low and low and mid move away one step.

                    nums[low],nums[mid] = nums[mid],nums[low]

                    mid += 1
                    low += 1

                elif nums[mid] == 1:
                    mid += 1
                else: #id mid == 2
                    nums[mid], nums[high] = nums[high] , nums[mid]
                    high -= 1
            return nums
        return func(nums)

