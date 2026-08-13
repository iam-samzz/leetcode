

def func(nums):

    pivot = 0

    i = 1
    j = len(nums) - 1

    
    while i < j:


        while i < j and nums[i] <= nums[pivot]:
            i += 1

        while i < j and nums[j] >= nums[pivot]:
            j -= 1

        if i < j:
            nums[i] , nums[j] = nums[j] , nums[i]

        
    nums[j] , nums[pivot] = nums[pivot] , nums[j]

    return nums

x = [0,43,32,5,5,65,-3,-55,-77,2,3,-4]

print(func(x))