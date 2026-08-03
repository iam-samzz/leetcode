class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        def function(s,k):
            sl = list(s)
            leng = len(sl)
            

            pointer = 0
            while pointer < leng:

                left = pointer
                if pointer+k-1 <len(sl):
                    right = pointer + k - 1
                else:
                    right = len(sl) -1
                while left < right:
                    sl[left],sl[right] = sl[right],sl[left]
                    left +=  1
                    right -= 1
                pointer += 2*k
             
            return "".join(sl)
        return function(s,k)