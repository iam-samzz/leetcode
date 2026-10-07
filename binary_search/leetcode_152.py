class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        n = len(nums)
        low = 0
        high = n - 1

        current_min = nums[high]

        while low <= high:
            mid = (low + high) // 2
            current_min = min(current_min , nums[mid])
            
            #finding the sorted part
            left_half = True if nums[low] <= nums[mid] else False
            right_half = True if nums[mid] <= nums[high] else False
            
            #if the left half is sorted
            if left_half:
                current_min = min(nums[low],current_min)
                low = mid + 1
                continue
            elif right_half:
                current_min = min(nums[mid+1],current_min)
                high = mid - 1
                continue
        return current_min