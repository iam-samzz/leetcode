class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        p1 = 1
        x = None
        y = None
        sorted_status = False
        while p1 < n:
            if nums[p1] < nums[p1 - 1]:
                x = p1
                y = p1-1
                
                break
            p1 += 1
        if x != None:
            # means the array is not sorted
            #how we know the pivot
            #using reversal algorithm lets sort the array

            # [4,5,6,7,  0,1,2]
            # 7,6,5,4, 2,1,0 -> [0,1,2    4,5,6,7]
            p1 = 0
            p2 = y
            while p1 < p2:
                nums[p1],nums[p2] = nums[p2],nums[p1]
                p1 += 1
                p2 -= 1
            p1 = x
            p2 = n - 1
            while p1 < p2:
                nums[p1],nums[p2] = nums[p2] , nums[p1]
                p1 += 1
                p2 -= 1

            p1 = 0
            p2 = n-1
            while p1 < p2:
                nums[p1] , nums[p2] = nums[p2] , nums[p1]
                p1 += 1
                p2 -= 1
            mini_arr_count_len = ( n-1 ) - x + 1
        else:
            sorted_status = True
            
        #array sorted
        # lets to binary search
        
        low = 0
        high = n-1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:

                if sorted_status:
                    return mid
                
                if mid < n-x:
                    return mid + x
                else:
                    return mid - (n - x)
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return -1