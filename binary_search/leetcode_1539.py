class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)
        for i in range(n):

            missing_so_far  = arr[i] - (i + 1)

            if missing_so_far >= k:
                if i == 0:
                    return k
                else:
                    # finding the missing_so_far for prev element
                    missing_prev  = arr[i-1] - ( (i-1) + 1)

                    #remaining k need from prev element to reach kth missing
                    remaining = k - missing_prev

                    # reached the exact location of kth missing
                    result = arr[i - 1] + remaining

                    return result
            

        #finding missing so far for a last element
        missing_so_far = arr[-1] - len(arr) -1 + 1


        # remaining needed from the last element
        remaining = k - missing_so_far

        result = arr[-1] + remaining

        return result

        



