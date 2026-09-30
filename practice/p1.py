# merge sorting


class Sort:
    def merge_sort(self,nums):
        if len(nums) <= 0:
            return "Empty list"
        elif len(nums) == 1:
            return nums
        
        def merge_sort_func(nums,low,high):

            if low == high:
                return

            mid = (low + high)//2
            merge_sort_func(nums,low,mid)
            merge_sort_func(nums,mid+1,high)

            merge(low,mid,high)

        def merge(low,mid,high):
            p1 = low
            p2 = mid + 1
            temp = []
            while p1 <= mid and p2 <= high:
                if nums[p1] <= nums[p2]:
                    temp.append(nums[p1])
                    p1 += 1
                elif nums[p2] < nums[p1]:
                    temp.append(nums[p2])
                    p2 += 1

                
                    

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
        
        low = 0
        high = len(nums) - 1
        merge_sort_func(nums,low,high)

if __name__ == "__main__":
    sort = Sort()
    arr = [9,-2,6,3,1092,-2983,484,1029,99,100,100,100]
    sort.merge_sort(arr)
    print(arr)
