
"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        set_len = len(s)
        arr_len = len(nums)

        if set_len < arr_len:
            return True
        else:
            return False