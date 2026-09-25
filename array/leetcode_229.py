# moore's voting algorithm extended

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1_count = 0
        candidate1 = None

        candidate2_count = 0
        candidate2 = None

        n = len(nums)
        for i in range(n):

            if candidate1_count == 0 and nums[i] != candidate2:
                candidate1 = nums[i]
                candidate1_count = 1
            elif candidate2_count == 0 and nums[i] != candidate1:
                candidate2 = nums[i]
                candidate2_count = 1

            elif nums[i] == candidate1:
                candidate1_count += 1

            elif nums[i] == candidate2:
                candidate2_count += 1

            else:
                candidate1_count -= 1
                candidate2_count -= 1
        x = []
        c1 = 0
        c2 = 0
        for num in nums:
            if num == candidate1:
                c1 += 1
            elif num == candidate2:
                c2 += 1
        
        if c1 > n // 3:
            x.append(candidate1)
        if c2 > n//3:
            x.append(candidate2)
        return x            