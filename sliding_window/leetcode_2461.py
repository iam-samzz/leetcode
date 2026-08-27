'''You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

    The length of the subarray is k, and
    All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.'''

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        

        def func(nums,k):

            n = len(nums)
            #window state
            window_hash = {}
            window_sum = 0
            #result state
            max_sum = 0

            left = 0

            for right in range(n):
                #adding into hash
                if nums[right] not in window_hash:
                    window_hash[nums[right]] = 1
                else:
                    window_hash[nums[right]] += 1

                #addidng into sum
                window_sum += nums[right]
                
                window_size = right - left + 1 #inclusive

                if window_size == k:

                    #the result state only accepts if all elements are distinct and len(window) = k

                    #we need to check 2 condition
                    #len(window_hash) == k, checks if all elements are unique

                    if len(window_hash) == k and window_size == k:
                        max_sum = max(max_sum,window_sum)
                    
                    
                    #dealing with left thing..
                    window_hash[nums[left]] -= 1
                    if window_hash[nums[left]] == 0:
                        del window_hash[nums[left]]

                    window_sum -= nums[left]

                    left += 1
            return max_sum
        return func(nums,k)


    