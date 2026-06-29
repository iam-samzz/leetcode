"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn]."""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length = len(nums)
        result = []
        length = round(length/2)

        for i in range(0,length):
            result.append(nums[i])
            result.append(nums[i+length])

        return result