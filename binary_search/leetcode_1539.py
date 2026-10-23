class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        for element in arr:
            if element <= k:
                k += 1
            else:
                return  k
        return k