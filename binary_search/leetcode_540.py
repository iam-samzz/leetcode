class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        low = 0
        high = n - 1


        # core idea is , the part with one single number have a length of odd
        # a part with only multiple numbers have a len of even

        while low <= high:
            if high - low + 1 == 1:
                return nums[low]
            #finding mid
            mid = (low + high) // 2
            #checking left of mid, right of mid
            if nums[mid + 1] == nums[mid]:
                mid = mid + 1
            elif nums[mid-1] == nums[mid]:
                mid = mid
            elif nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
                
            #now mid is at last pos of mid pair
            left_len = mid - low + 1
            
            if left_len % 2 == 0:
                low = mid + 1
            else:
                mid -= 1
                high = mid - 1
        return nums[mid]
