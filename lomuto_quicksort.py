def partition(nums):

    i = 0
    #j = 0 through loop

    pivot = len(nums)-1

    for j in range(0,len(nums)-1): # we are going until len(n) - 2

        if nums[j] <= nums[pivot]:
            nums[j],nums[i] = nums[i] , nums[j] #swapping i-element and j-element
            i += 1

    nums[i] , nums[pivot] = nums[pivot], nums[i]
    

    return i


def func(nums):


    if len(nums) <= 1:
        return nums
    # do the partition for the list
    # keep the current sorted element
    #recursively do partition for left, 
    #recursively do partiiton for righ

    #base case: if its just 2 element in a list, just do partition and return
    correct_index = partition(nums)

    #left list
    left = func(nums[:correct_index])

    #right list
    right = func(nums[correct_index+1:])


    return left + [nums[correct_index]] + right


nums = [9,3,2,3,0,-1]
print(func(nums))