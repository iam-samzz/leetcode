'''Given an array of positive integers, find the minimum length of a subarray whose sum is >= target sum.'''

'''Example: nums = [2, 3, 1, 2, 4, 3], target = 7. (Answer is 2, from [4, 3]).'''



def func(nums,target):

    n = len(nums)

    left = 0

    #window state
    winSum = 0

    #result state
    minLenSubarray = None

    for right in range(n):
        winSum += nums[right]

        if winSum >= target:
            #moving left
            while left <= right and winSum >= target:

                if minLenSubarray == None:
                    minLenSubarray = right - left + 1
                else:
                    minLenSubarray = min(minLenSubarray , right-left+1)

                winSum -= nums[left]

                left += 1
    return minLenSubarray

nums = [2, 3, 1, 2, 4, 3]
target = 7

print(func(nums,target))