class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        def func(nums1,nums2):
            h1 = {}
            h2 = {}
            result = []
            for i in range(len(nums1)):
                #frequency
                if nums1[i] not in h1:
                    h1[nums1[i]] = 1
                else:
                    h1[nums1[i]] += 1
                
            for i in range(len(nums2)):
                 # feequency

                if nums2[i] not in h2:
                    h2[nums2[i]] = 1
                else:
                    h2[nums2[i]] += 1
            
            #iterate through h2 
            for e in h2:
                if e in h1:
                    min_freq = min(h2[e],h1[e])
                    for i in range(min_freq):
                        result.append(e)
            return result
        return func(nums1,nums2)
            