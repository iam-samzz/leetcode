class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        

        #finding 1st one
        left = 0
        while left < len(nums) and nums[left] != 1:
            left += 1
        
        
            #now left is at 1st one
        right = left + 1
        
        while right < len(nums):

            if nums[right] == 1:
                #check distance

                #right - left - 1 gives the number of boxed b/w right and left, excluding the right box and left box.
                if right - left - 1 < k:
                    return False
                elif right - left >= k:
                    left = right
            right += 1
        return True
