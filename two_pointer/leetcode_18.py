class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        
        def func(nums):
            nums.sort()

            result = []
            for a in range(len(nums)-2):
                
                if (nums[a]!= nums[a-1] and a!= 0) or a==0:
                    #i.e when nums[a] == 0 or nums[a] != nums[a-1]
                    for b in range(a+1,len(nums)):
                        #
                        # code

                        if (nums[b] != nums[b-1] and b!=a+1) or b == a+1:
                            left = b+1
                            right = len(nums) - 1

                            while left < right:
                                s = nums[a] + nums[b] + nums[left] + nums[right]

                                if s == target:
                                    result.append([nums[a],nums[b],nums[left],nums[right]])
                                    left += 1
                                    while nums[left] == nums[left-1] and left < right:
                                        left += 1

                                    right -= 1
                                    while nums[right] == nums[right + 1] and left < right:
                                        right -= 1


                                elif s < target:
                                    left += 1
                                    while nums[left] == nums[left-1] and left < right:
                                        left += 1
                                else:
                                    right -= 1
                                    while nums[right] == nums[right + 1] and left < right:
                                        right -= 1
                                
            return result
        return func(nums)
