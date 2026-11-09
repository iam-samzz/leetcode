class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # --- Step 1: always binary-search on the SMALLER array ---
        # This keeps the loop at O(log(min(m, n))) and guarantees
        # the "other side" split never goes out of bounds.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        # --- Step 2: how big is the "left half" of the merged array? ---
        # Odd total -> left half gets one extra element (the median).
        # (m + n + 1) // 2 is the same as math.ceil((m + n) / 2).
        left_size = (m + n + 1) // 2

        # --- Step 3: binary search "how many from nums1 go to the left half" ---
        # If we take i elements from nums1, we must take (left_size - i)
        # from nums2 so that the total left-half count matches.
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2      # count from nums1  (left half)
            j = left_size - i       # count from nums2  (left half)

            # --- Step 4: read the 4 boundary values, using ±inf as sentinels ---
            a_left  = nums1[i - 1] if i > 0 else float('-inf')
            a_right = nums1[i]     if i < m else float('inf')
            b_left  = nums2[j - 1] if j > 0 else float('-inf')
            b_right = nums2[j]     if j < n else float('inf')

            # --- Step 5: is the partition valid? ---
            # Valid iff every element on the left <= every element on the right.
            # Since each array is sorted, we only need to check the 2 seams.
            if a_left > b_right:
                hi = i - 1          # took too many from nums1 -> shrink
            elif b_left > a_right:
                lo = i + 1          # took too few   from nums1 -> grow
            else:
                # Partition is valid — compute the median
                max_left  = max(a_left, b_left)
                min_right = min(a_right, b_right)

                if (m + n) % 2 == 1:
                    return max_left                     # odd: median sits in left half
                return (max_left + min_right) / 2       # even: average of the middle two