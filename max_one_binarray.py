#fixed sliding window

def func(nums,k):

    n = len(nums)

    #window state
    no_of_ones_in_window = 0

    #result state
    max_ones = 0

    left = 0

    for right in range(n):

        if nums[right] == 1:
            no_of_ones_in_window += 1

        win_size = right - left + 1

        if win_size == k:

            max_ones = max(max_ones,no_of_ones_in_window)

            if nums[left] == 1:
                no_of_ones_in_window -= 1

            left += 1

    return max_ones

print(func([1, 0, 1, 1, 0, 1],3))