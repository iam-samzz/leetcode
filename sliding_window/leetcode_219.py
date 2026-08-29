class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        def func(nums,k):

            n = len(nums)
            window = set()
            left = 0

            for right in range(n):

                distance = right - left

                #case 1
                if distance <= k:

                    if nums[right] not in window:
                        window.add(nums[right])
                    else:
                        return True
                

                #case 2
                elif distance > k:

                    window.remove(nums[left])
                    left += 1

                    if nums[right] not in window:
                        window.add(nums[right])
                    else:
                        return True
                
            return False
        return func(nums,k)