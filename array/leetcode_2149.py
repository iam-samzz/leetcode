class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        n= len(nums)

        result = [0]*n

        pos = 0
        neg = 0

        p = 0
        p_s = True

        while p < n:
            if p_s == True:
                while nums[pos] < 0:
                    pos += 1
                result[p] = nums[pos]
                pos+=1
                
                p_s = False
            elif p_s == False:
                while nums[neg] > 0:
                    neg += 1
                result[p] = nums[neg]
                neg+=1
                p_s = True
            p+=1
        return result
            

        
        