class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #reads nums1 elements from back
        read1 = m-1
        #reads nums2 elements from back
        read2 = n-1
        #reads nums2 from 0's to write it from back
        write = m + n - 1

        #we are going from backward of nums1,  since we have to do it in O(1) space,
        #we are ordering higher element 1st
        # note : the buffer zone i.e  the 0 zone will get increase once we put some element from the same array into buffer zone

        while read1 >= 0 and read2 >= 0:
            if nums1[read1] > nums2[read2]:
                nums1[write] = nums1[read1]
                write -= 1
                read1 -= 1
            elif nums2[read2] > nums1[read1]:
                nums1[write] = nums2[read2]
                write -= 1
                read2 -= 1
            else:
                nums1[write] = nums1[read1]
                write -= 1
                read1 -= 1

                nums1[write] = nums2[read2]
                write -= 1
                read2 -= 1

        while read1 >= 0:
            nums1[write] = nums1[read1]
            write -= 1
            read1 -= 1
        while read2 >= 0:
            nums1[write] = nums2[read2]
            write -= 1
            read2 -= 1
        return nums1
            
#explanation : https://share.google/aimode/nBFag1AJlNiw6QImc