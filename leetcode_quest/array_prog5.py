"""Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array."""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        

        def find(nums):
            
            l = len(nums)
            count = 0

            result = []
            for i in range(0,l):
                for j in range(0,l):
                    if nums[j] < nums[i]:
                        count = count + 1

                result.append(count)
                count = 0

            return result
        
        return find(nums)

                    