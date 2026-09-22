class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)

        max_l = 0

        for element in nums_set:
            if element-1 not in nums_set:
                #its the starting of the sequence
                z = 1
                while (element+z) in nums_set:
                    z += 1
                max_l = max(max_l,z)
        
        return max_l

            