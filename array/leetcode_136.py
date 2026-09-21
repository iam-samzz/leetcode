class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        nums.sort()
        n = len(nums)
        left = 1
        count = 1
        while left < n:
            if nums[left] != nums[left - 1]:
                #check the count 
                if count < 2:
                    return nums[left - 1]
                elif count == 2:
                    count = 1
            elif nums[left] == nums[left - 1]:
                count += 1
            left += 1
        return nums[-1]


#done using O(n.logn) time complexity and O(1) space complexity
# we can acheive O(n) time comeplexity using bit manupulation
