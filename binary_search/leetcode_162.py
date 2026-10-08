class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        if n == 1:
            return 0

        if nums[low + 1] < nums[low]:
            return low
        if nums[high - 1] < nums[high]:
            return high
        
        low = 1
        high = n-2

        while low <= high:
            mid = (low + high) // 2

            # its a peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            # mid is in b/w in increasing order
            elif nums[mid] > nums[mid - 1] and nums[mid]  < nums[mid + 1]:
                low = mid + 1
            
            #decreasing..
            elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
                high = mid - 1

            elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                high = mid - 1