class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        

        def func(nums):
            nums.sort()

            # there is some target
            # if the sum should be closest, it should greater , equal , or less than, but shorter.

            non_equal = nums[0] + nums[1] +nums[2]
            for a in range(len(nums)):

                if (nums[a] != nums[a-1] and a!=0) or a==0:

                    left = a+1
                    right = len(nums) - 1
                    
                    while left < right:
                        s = nums[a] + nums[left] + nums[right]
                        if s == target:
                            return s
                        
                        elif s < target:
                            if abs(target-s) < abs(target - non_equal):
                                non_equal = s
                            left += 1
                        else:
                            if abs(target - s) < abs(target - non_equal):
                                non_equal = s
                            right -= 1
                        
                                
                     
                    """left += 1
                    right -= 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1

                    while nums[right] == nums[right+1] and left < right:
                        right -= 1"""
            return non_equal
                        

        return func(nums)



        