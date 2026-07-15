class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        num3 = []
        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                nums1.append(nums1[p1])
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                nums1.append(nums2[p2])
                p2 += 1
            else:
                nums1.append(nums1[p1])
                nums1.append(nums2[p2])

                p1 += 1
                p2 += 1
        if p1 < m:
            for i in range(p1,m):
                nums1.append(nums1[i])
        elif p2 < n:
            for i in range(p2,n):
                nums1.append(nums2[i])
        del nums1[:n+m]

