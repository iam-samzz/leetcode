class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        

        #basically we need the magnitude of value  inside the abs func as high
        #so we need to get both max subarray sum and minimum subarray sum, because those only have high magnitude
        length = len(nums)

        max_sum = nums[0]
        min_sum = nums[0]

        current_sum1 = nums[0]
        current_sum2 = nums[0]

        m = 1 #max pointer
        n = 1 #min pointer

        while m < length and n < length:
            #using kadane for finding max_sum
            current_sum1 += nums[m]
            if current_sum1 < nums[m]:
                current_sum1 = nums[m]
            
            max_sum = max(max_sum , current_sum1)
            m += 1

            #using kadane for finding min_sum

            current_sum2 += nums[n]
            if current_sum2 > nums[n]:
                current_sum2 = nums[n]
            
            min_sum = min(min_sum , current_sum2)
            n += 1
        max_sum = abs(max_sum)
        min_sum = abs(min_sum)

        return max(max_sum, min_sum)


