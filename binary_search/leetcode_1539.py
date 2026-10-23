class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)

        low = 0
        high = n - 1

        while high - low  + 1 > 2:
            mid = (low + high ) // 2
            
            #find mid's current missing_so_for state

            missing_so_far = arr[mid] - (mid + 1)

            if missing_so_far < k:
                low = mid

            elif missing_so_far >= k:
                high = mid


        # now we got 2 ranges
        if arr[high] - (high + 1) >= k and arr[low] - (low + 1) < k:

            #high
            remaining = k - (arr[low] - (low + 1))
            result = arr[low]  + remaining

            return result

        elif arr[high] - (high + 1) < k and arr[low] - (low + 1) < k:
            high = -1
            missing_so_far = arr[high] - (high + 1)

            remaining = k - missing_so_far 

            result = arr[high] + remaining

            return result
        elif arr[low] - (low + 1) >= k :
            return k

                

        



