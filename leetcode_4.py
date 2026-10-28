import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        #note : note in bianry search we are not searching for elements!!!!, we are searching for how many elemen

        m  = len(nums1)
        n =  len(nums2)

        left_half_count  = math.ceil((m + n) / 2 )

        if n < m:
            #choose n for binary search (i.e nums2)
            search = nums2
            non_search = nums1
            search_len = n
            non_search_len = m
            low = 0
            high = n 
        else:
            #choose m for binary search (i.e nums 1)
            search = nums1
            non_search = nums2
            search_len = m 
            non_search_len = n
            low = 0
            high = m 
        
        while low <= high:

            # here mid is the number of elements in left side for arr 1
            split1 = (low + high) // 2
            split2 = left_half_count - split1

            left_1 = float('-inf') if split1 == 0  else search[split1 - 1]
            right_1 = float('inf') if split1 == search_len else search[split1]

            left_2 = float('-inf') if split2 == 0 else non_search[split2 - 1]
            right_2 = float('inf') if split2 == non_search_len else non_search[split2]

            if left_1 > right_2:
                high = split1 - 1
            elif left_2 > right_1:
                low = split1 + 1
            else:

                if (m + n) % 2 != 0:
                    #odd 
                    return max(left_1 , left_2)
                else:
                    return (max(left_1 , left_2) + min(right_1 , right_2 )) / 2


