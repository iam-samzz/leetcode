# brute force method

class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        

        max_days = max(bloomDay)
        
        for i in range(1,max_days+1):
            count = 0
            adj = 0

            for j in range(len(bloomDay)):

                if bloomDay[j] <= i:
                    adj += 1
                    if adj == k:
                        count += 1
                        adj = 0
                else:
                    adj = 0
                

            if count >= m:
                return i
        return -1


