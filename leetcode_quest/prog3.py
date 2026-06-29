"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        def find_max_1(list):
            if len(list) == 0:
                return 0
            count = 0
            result = []
            for i in range(0,len(list)-1):
                if list[i] == 1:
                    count = count + 1
                else:
                    result.append(count)
                    count = 0
            if list[-1] == 1:
                count = count + 1
                result.append(count)
            if list[-1] == 0:
                result.append(count)
                
            if len(result)!=0:
                m = max(result)
                return m
            else:
                return 0


        return find_max_1(nums)