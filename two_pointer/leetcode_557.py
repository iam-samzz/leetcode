class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_list = list(s)
        pointer = 0
        pointer2 = 0
        while pointer < len(s_list):
            if pointer == len(s_list) - 1:
                right = pointer

                while pointer2 < right:
                    s_list[pointer2],s_list[right] = s_list[right],s_list[pointer2]
                    pointer2 += 1
                    right -= 1
                
                
            if s_list[pointer] == ' ':
                right = pointer - 1
                while pointer2 < right:
                    s_list[pointer2],s_list[right] = s_list[right],s_list[pointer2]
                    pointer2 += 1
                    right -= 1

                pointer2 = pointer + 1
            pointer += 1
        return "".join(s_list)
                
            
            
