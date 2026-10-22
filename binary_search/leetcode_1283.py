import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        

        max_divisor = max(nums)
        n = len(nums)
        low = 1
        high = max_divisor
        min_divisor = -1
        while low <= high:
            mid = ( low + high ) // 2
            s = 0
            #for this mid, lets find the summation for the array divisions
            for i in range(n):

                divident = nums[i]
                divisor = mid
                quotient = math.ceil( divident / mid )
                

                s += quotient


            # if s is more, we still need less reminders, so we need big divisors
            if s > threshold:
                low = mid + 1

            elif s <= threshold:
                min_divisor = mid
                high = mid - 1
        return min_divisor