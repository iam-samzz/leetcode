class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        

        def func(nums):

            length = len(nums)
            pivot = None

            for i in range(length-2,-1,-1):
                if nums[i] < nums[i+1]:
                    pivot = i
                    break
            #completely reversed, that is whole number reached its max arrangement 
            if pivot == None:
                left = 0
                right = length - 1
                while left < right:
                    nums[left] , nums[right] = nums[right],nums[left]
                    left += 1
                    right -= 1
                return nums

            # now swap the element with next largest element from the suffix

            #finding the swap element
            #since the suffix is already sorted reversly, we can go through one single way

            #finding nearest greater number
            for i in range(length-1,pivot,-1):
                if nums[i] > nums[pivot]:
                    nums[i],nums[pivot] = nums[pivot],nums[i]
                    break
                
            #now its swapped.
            #just reverse the suffix
            left = pivot + 1
            right = length - 1
            while left < right:
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1
                right -=1
            return nums
        return func(nums)    
