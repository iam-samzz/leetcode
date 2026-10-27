class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        def check_combination(mid, k ):
            s = 0
            count = 1
            for i in range(n):
                if s + nums[i] <=  mid:
                    s += nums[i]
                else:
                    count += 1
                    s = nums[i]
            if count <= k:
                return True
            else:
                False
                

        # at any compbination , the minimum possible highest sum is max(nums)
        low = max(nums)

        # maximum possible highest sum is sum(arr)

        high = sum(nums)
        min_sum = None
        while low <= high:

            mid = (low + high ) // 2 

            if check_combination(mid, k ):
                min_sum = mid
                high = mid - 1
            else:
                low = mid  + 1
        
        return min_sum


