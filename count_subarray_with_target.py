#fixed sliding window

'''Count Subarrays with Sum Above Target

    Task: Given an integer array nums, a window size k, and a target number target,
      count how many windows of size k have a total sum strictly greater than target.'''

def func(nums,k,target):

    n = len(nums)

    #window state 
    window_sum = 0

    #result state
    count_target_sum = 0

    left = 0

    for right in range(n):
        window_sum += nums[right]

        window_size = right - left + 1

        if window_size == k:
            if window_sum > target: # if they asked equal to target, we check "if window == target:"
                count_target_sum += 1

            window_sum -= nums[left]
            left += 1

        #right ++ done y loop automatically
    return count_target_sum

print(func([4, 2, 1, 7, 8, 1, 2],3,10))
