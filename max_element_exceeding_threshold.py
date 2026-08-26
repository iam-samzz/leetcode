#fixed sliding window

'''Maximum Elements Exceeding Threshold

    Task: Given an integer array nums, a window size k, and a limit val, 
    find the maximum number of elements strictly greater than val present in any window of size k.'''
def func(nums,k,val):
    n = len(nums)
    
    if k > n or k <= 0:
        return 0
    
    #window state
    win_count_val_greater = 0

    #result state
    max_count = 0

    left = 0

    for right in range(n):
        if nums[right] > val:
            win_count_val_greater += 1

        win_size = right - left + 1

        if win_size == k:
            max_count = max(max_count,win_count_val_greater)

            if nums[left] > val:
                win_count_val_greater -= 1
            left += 1
    return max_count

print(func([10, 2, 15, 20, 3, 5],3,8))