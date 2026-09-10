

#bubble sort



def func(nums):
    i = 0
    j = 0
    n = len(nums)

    while i < n:
        j = 0
        swapped = False
        while j < n - 1 - i:
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1] ,nums[j]
                swapped = True
            j += 1
        if swapped == False:
            break
        i += 1
    return nums

if __name__ == "__main__":
    l = [9,8,4,4387,-232]
    print(func(l))