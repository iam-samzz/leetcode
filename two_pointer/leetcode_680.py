class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        #normal palindrome checking

        def check(s_list,skip):
            left = 0
            right = len(s_list) - 1


            while left < right:
                if left == skip:
                    left += 1
                    continue
                if right == skip:
                    right -= 1
                    continue
                
                if s_list[left] != s_list[right]:
                    return [left,right]
                left += 1
                right -= 1
            return True
        
        def func(s_list):
            status = check(s_list,None)
            if status == True:
                return True
            else:

                if check(s_list,status[0]) == True:
                    return True
                else:
                    
                    if check(s_list,status[1]) == True:
                        return True
                    else:
                        return False
                    
        
        return func(s)