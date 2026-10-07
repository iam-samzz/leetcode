class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            #find the sorted parts
            left_half_sorted_status = True if nums[low] <= nums[mid] else False
            right_half_sorted_status = True if nums[mid] <= nums[high] else False

            #if the left half is sorted
            if left_half_sorted_status:
                #checking if target is inside in this sorted area
                if nums[low] <= target <= nums[mid]:
                    #if the target is within this range,reducing the search space to this range
                    high = mid - 1
                else:
                    low = mid + 1
            elif right_half_sorted_status:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False