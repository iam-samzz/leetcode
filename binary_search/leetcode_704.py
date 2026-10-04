class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        low = 0
        high = len(nums) - 1
        ans = None
        def r(arr,low,high):
            #base case
            if low > high:
                return -1
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                ans = r(arr,mid+1,high)
            else:
                ans = r(arr,low,mid-1)
            
            return ans
        def iterative(arr,low,high):
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        return iterative(nums,low,high)