class Solution:
    def isPalindrome(self, s: str) -> bool:


        def valid(s):

            s = s.lower()

            result = []
            for i in s:
                if i.isalnum():
                    result.append(i)
            if len(result) <= 1:
                return True
            final = "".join(result)


            #checking palindrome

            left = 0
            right = len(final) -1 

            status = False
            while left < right:
                if final[left] == final[right]:
                    status = True
                else:
                    status = False
                    break    
                left += 1
                right -= 1
            return status

        return valid(s)
    
            
