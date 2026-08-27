class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        i = 0

        for j in range(len(nums)):

            # Condition 1: current distance is valid
            if j - i <= k:

                if nums[j] in window:
                    return True

                window.add(nums[j])

            # Condition 2: current distance is too large
            else:
                window.remove(nums[i])
                i += 1

                # Now check again with the new i
                if nums[j] in window:
                    return True

                window.add(nums[j])

        return False
