def func(nums,k,t):

    count = 0
    window_avg = 0

    #we need to check avg of every window and count ++ if avg >= t

    left = 0
    right = k - 1

    #1st window avg
    window_avg = sum(nums[left:right+1]) / k

    if window_avg >= t:
        count += 1

    while right <= len(nums) - 2:

        window_avg = window_avg - ( nums[left] / k)
        left += 1

        right += 1
        window_avg = window_avg + (nums[right] / k)


        if window_avg >= t:
            count += 1
    return count
