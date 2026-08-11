# sample list [2,3,66,85,1,-8,99,32,34,43902,22,22,0]

nums = [2,3,66,85,1,-8,99,32,34,43902,22,22,0,22]

def func(nums):

    i = 0
    #j = 0 through loop

    pivot = len(nums)-1

    for j in range(0,len(nums)-1): # we are going until len(n) - 2

        if nums[j] <= nums[pivot]:
            nums[j],nums[i] = nums[i] , nums[j] #swapping i-element and j-element
            i += 1

    if nums[i] > nums[pivot]:
        nums[i] , nums[pivot] = nums[pivot] , nums[i]
    elif nums[i] <= nums[pivot]:
        i += 1
        nums[i] , nums[pivot] = nums[pivot], nums[i]
        i -= 1

    return nums,i
        

 
print(func(nums))