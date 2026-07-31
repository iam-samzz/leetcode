class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        def function(nums1,nums2):

            nums1 = set(nums1)
            nums2 = set(nums2)

            result = []

            for element in nums1:
                if element in nums2:
                    result.append(element)
            return result
        return function(nums1,nums2)