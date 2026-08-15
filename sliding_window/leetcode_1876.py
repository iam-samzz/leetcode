class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3

        def func(nums):
            if len(nums) < k:
                return 0
            left = 0
            right = k - 1
            count = 0

            h = {}

            for i in range(k):
                if nums[i] not in h:
                    h[nums[i]] = 1
                else:
                    h[nums[i]] += 1
                if len(h) == k:
                    count += 1

            while right <= len(nums) - 2:
                if nums[left] in h:
                    h[nums[left]] -= 1

                    if h[nums[left]] == 0 : # if only one element was there
                        del h[nums[left]]
                left += 1

                right += 1
                if nums[right] not in h:
                    h[nums[right]] = 1
                else:
                    h[nums[right]] += 1

                if len(h) == k:
                    count += 1
            return count
        return func(s)
