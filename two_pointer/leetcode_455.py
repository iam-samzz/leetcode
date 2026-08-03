class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        def function(g,s):

            i = 0 #for the g (greed factor)
            count = 0
            for j in range(len(s)):
                if i > len(g)-1:
                    break
                if s[j] >= g[i]:
                    count += 1
                    i += 1
            return count
        
        

        #sort:
        def sort(lis):

            if len(lis)<=1:
                return lis

            mid =  len(lis) // 2

            left = sort(lis[:mid])
            right = sort(lis[mid:])

            return merge(left,right)
        def merge(left,right):
            lef_p = 0
            rig_p = 0
            mer = []

            while (lef_p < len(left)) and (rig_p < len(right)):
                if left[lef_p] < right[rig_p]:
                    mer.append(left[lef_p])
                    lef_p += 1
                elif right[rig_p] < left[lef_p]:
                    mer.append(right[rig_p])
                    rig_p += 1
                else:
                    mer.append(left[lef_p])
                    lef_p += 1
                
            while lef_p < len(left):
                    mer.append(left[lef_p])
                    lef_p += 1
            while rig_p < len(right):
                    mer.append(right[rig_p])
                    rig_p += 1
                
            return mer
        sorted_g = sorted(g) #using in build sorted method for reducing the space complexity
        sorted_s = sorted(s) # "              "             "          "
        return function(sorted_g,sorted_s)
        
        
        
