class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        n = len(nums)
        low1 = 0
        high1 = n - 1
        ans1 = None

        low2 = 0
        high2 = n - 1
        ans2 = None

        
        while low1 <= high1:
            mid = (low1 + high1) // 2
            if nums[mid] < target:
                low1 = mid + 1
            elif nums[mid] >= target:
                ans1 = mid
                high1 = mid - 1
        if ans1 ==None or ans1 > n-1 or nums[ans1] != target:
            return [-1,-1]
        else:
            while low2 <= high2:
                mid = (low2 + high2) // 2

                if nums[mid] <= target:
                    ans2 = mid
                    low2 = mid + 1
                elif nums[mid] > target:
                    high2 = mid - 1
            if ans2 == None or ans2 > n-1:
                return [-1,-1]
            return [ans1,ans2]
        

