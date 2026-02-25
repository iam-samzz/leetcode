class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index = 0
        jindex = 0
        for i in nums:
            
            #[1,2,3,4] --> so no repatition
            #
            jindex = index + 1
            if index < len(nums)-1:
                for j in nums[jindex:]:
                    if i+j == target and index != jindex:
                        l = [index,jindex]
                        return l
                    jindex = jindex +1 
                    

                    
            index = index + 1

i = Solution()
i.twoSum([1,2,3],3)
                
