class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        

        max_days = max(bloomDay)
        low = 1
        high = max_days

        min_day = -1
        while low <= high:
            # mid = i
            i = (low + high) // 2
            adj = 0
            count = 0
            for j in range(len(bloomDay)):
                if bloomDay[j] <= i:
                    adj += 1
                    if adj == k:
                        count += 1
                        adj = 0
                else:
                    adj = 0
            if count >= m:
                min_day = i
                high = i - 1
            elif count < m:
                low = i + 1
        
        return min_day
