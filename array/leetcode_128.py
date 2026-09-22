class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if len(nums) <=0:
            return 0
        
        nums.sort()
        
        
        left = 1
        c=1
        max_l = 1

        while left < len(nums):
            if nums[left] == nums[left-1]:
                left += 1
            elif nums[left] == nums[left-1]+1:
                c += 1
                max_l = max(max_l,c)
                left += 1
            else:
                c = 1
                max_l = max(max_l,c)
                left +=1

        return max_l