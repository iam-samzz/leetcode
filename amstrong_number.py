class Solution:
    def armstrongNumber (self, n):
        # code here 
        x = n
        ams = 0
        
        for i in range(3):
            ams += (n%10) ** 3
            n = n // 10
        if ams == x:
            
            return True
        else:
            return False
        