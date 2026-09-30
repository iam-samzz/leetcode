class Solution:
    def inversionCount(self, arr):
        # code here
        def merge_sort(nums):
            if len(nums) <= 0:
                return "Empty list"
            elif len(nums) == 1:
                return nums

            def merge_sort_func(nums,low,high):

                if low == high:
                    return 0

                mid = (low + high)//2
                count_left = merge_sort_func(nums,low,mid)
                count_right = merge_sort_func(nums,mid+1,high)

                count_after_merge = merge(low,mid,high)

                return count_left + count_right + count_after_merge

            def merge(low,mid,high):
                p1 = low
                p2 = mid + 1
                temp = []
                count = 0
                while p1 <= mid and p2 <= high:
                    if nums[p1] < nums[p2]:
                        temp.append(nums[p1])
                        p1 += 1
                    elif nums[p2] < nums[p1]:
                        temp.append(nums[p2])
                        p2 += 1
                        
                        
                        count += (mid - p1 + 1)
                        
                    else:
                        temp.append(nums[p1])
                        temp.append(nums[p2])
                        p1 += 1
                        

                while p1 <= mid:
                    temp.append(nums[p1])
                    p1 += 1
                while p2 <= high:
                    temp.append(nums[p2])
                    p2 += 1

                p = low
                tp = 0
                while p <= high:
                    nums[p] = temp[tp]
                    p += 1
                    tp += 1
                return count
            low = 0
            high = len(nums) - 1
            
            return merge_sort_func(nums,low,high)
        return merge_sort(arr)