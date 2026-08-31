class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        left = 0
        count = [0] * 51
        res = []

        for right in range(len(nums)):

            # Add right element
            if nums[right] < 0:
                count[abs(nums[right])] += 1

            # Window reached size k
            if right - left + 1 == k:

                # Find x-th smallest negative
                found = 0
                answer = 0

                for index in range(50, 0, -1):

                    found += count[index]

                    if found >= x:
                        answer = -index
                        break

                res.append(answer)

                # Remove left element
                if nums[left] < 0:
                    count[abs(nums[left])] -= 1

                left += 1

        return res