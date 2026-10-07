class Solution:
    def search(self, nums: list[int], target: int) -> int:

        n = len(nums)
        low = 0 
        high = n - 1

        while low <= high:
            
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            else:
                #sorted status
                left_half = True if nums[low] <= nums[mid] else False
                right_half = True if nums[mid] <= nums[high] else False
                #left half is sorted inclusive of mid
                if left_half:
                    # check wheather the  target is within this range
                    #if yes: then search inside it.
                    # if no reduce the search space to right half

                    if nums[low] <= target <= nums[mid]:
                        high = mid - 1
                    else:
                        low = mid+1
                
                #right half is sorted inclusive of mid
                elif right_half:
                    #check wheather the target is within this range
                    # if yes, do binary search b.w this space
                    #if no, then reduce the space to left half

                    if nums[mid] <= target <= nums[high]:
                        low = mid + 1
                        
                    else:
                        high = mid - 1
        return -1