class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_prefix_sum = 0
        prefix_map = {0:1}
        count = 0
        n = len(nums)
        for i in range(n):
            current_prefix_sum += nums[i]

            #required
            prev_prefix_sum = current_prefix_sum - k
            
            if prev_prefix_sum in prefix_map:
                count += prefix_map[prev_prefix_sum]
            
            if current_prefix_sum not in prefix_map:
                prefix_map[current_prefix_sum] = 1
            else:
                prefix_map[current_prefix_sum] += 1
        return count
