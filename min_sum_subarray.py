# fixed size sliding window

def func(nums,k):

    n = len(nums)
    left = 0

    #window state
    win_sum = 0

    #result state
    min_sum = None

    #loop flow: right increment -> update -> left decrement -> right increment-> update-> ...

    for right in range(n):
        
        win_sum += nums[right]

        if right - left + 1 == k:
            if min_sum:
                min_sum = min(win_sum,min_sum)
            else:
                min_sum = win_sum
            
            win_sum -= nums[left]
            left += 1
    return min_sum

print(func([3, 7, 9, 1, 2, 4],2))