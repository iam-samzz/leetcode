#fixed sliding window

def func(nums,k):

    n = len(nums)

    #window state  
        #no.of even numbers in a window
    window_even_count = 0

    #result state
    max_even = 0

    #left wall of a window
    left = 0

    for right in range(1,n+1):
        
        if nums[right - 1] % 2 == 0:
            window_even_count += 1

        #inclusive window size
        window_size = right - left
        if window_size >= k:

            #check and update
            max_even = max(max_even,window_even_count)

            #remove left values from window
            if nums[left] % 2 == 0:
                window_even_count -= 1

            left += 1
    return max_even

print(func([1, 2, 4, 3, 6, 8, 10, 1],3))





    