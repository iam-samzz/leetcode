class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        def func(nums,k):
            left = 0
            right = k - 1
            window_avg = 0

            #summing the 1st window
            window_avg = sum(nums[:k]) / k
            max_avg = window_avg

            left = 0


            while right < len(nums)-1:

                window_avg = window_avg - (nums[left]/k)
                left += 1

                right += 1
                window_avg = window_avg + (nums[right]/k)

                max_avg = max(window_avg,max_avg)
            return max_avg
        return func(nums,k)
