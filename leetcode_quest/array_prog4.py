class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        

        def find(nums):
            

            seen = set()
            
            result = []

            for i in nums:
                if i in seen:
                    result.append(i)
                else:
                    seen.add(i)

            for i in range(1,len(nums)+1):
                if i not in seen:
                    result.append(i)
            return result
        return find(nums)



