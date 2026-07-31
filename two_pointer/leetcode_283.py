class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def function(nums):
            
            write = 0 #at the 1st location -> its slow
            
            for read in range(len(nums)):
                
                if nums[read] != 0:
                    # swp to write
                    if read != write:    
                        nums[write],nums[read] = nums[read],0
                    write += 1

        function(nums)
