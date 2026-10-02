class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        n = len(nums)
        prefix_product = 1
        suffix_product = 1

        prefix_p = 0
        suffix_p = n - 1

        prefix_max = float('-inf')
        suffix_max = float('-inf')

        while prefix_p < n:
            prefix_product *= nums[prefix_p]
            if prefix_product == 0:
                prefix_product = 1
                prefix_max = max(prefix_max , 0)
            else:
                prefix_max = max(prefix_max , prefix_product)
            prefix_p += 1

            suffix_product *= nums[suffix_p]
            if suffix_product == 0:
                suffix_product = 1
                suffix_max = max(suffix_max, 0)
            else:
                suffix_max = max(suffix_max , suffix_product)
            suffix_p -= 1
        
        return max(suffix_max , prefix_max)