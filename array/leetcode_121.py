class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        n = len(prices)
        left = 0
        right= 0

        max_p = float('-inf')

        while right < n:
            diff = prices[right] - prices[left]

            if diff < 0:
                left = right
            elif diff > 0:
                max_p = max(max_p,diff)
            right += 1
        if max_p == float('-inf'):
            return 0
        return max_p
            