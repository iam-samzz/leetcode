class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        

        length = len(nums)
        s = set(nums)

        result = []
        for i in range(1,length+1):
            if i not in s:
                result.append(i)
            
        return result

"""Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums."""