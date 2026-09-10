def selection_sort(nums):
    n = len(nums)
    i = 0
    min_index = 0
    
    while i < n:
        j = i
        while j < n:
            if nums[j] < nums[min_index]:
                min_index = j
            j += 1

        nums[i],nums[min_index] = nums[min_index],nums[i]
        i += 1
        min_index = i
    return nums

if __name__ == "__main__":
    print(selection_sort([9,4,100,9930,29387,0,-88]))
