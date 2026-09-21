class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        left = 0
        right = n-1
        k = k % n
        #reverse the array
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            right -= 1
            left += 1
        
        #reverse 1st k element
        left = 0
        right = k - 1

        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1

        #reverse remaining element
        left = k
        right = n - 1

        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        return nums
        

        