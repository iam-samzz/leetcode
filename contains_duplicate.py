class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """-get the list
            - what is duplicate?
                if number repared twice,
            how it can repeat twice?
                -one method we can create another array and check the original array with that/
                -create for loop twice and iterate through n^2
                -for i in array
                   
                    find the number i from the list.

                    [,2,3,4,5] , [1]

                

                """
        status = False
        checked = {}
        index = 0
        for i in nums:

            if i in checked:  #element : index
                status = True
                break
            else:
                checked[i] = index
            
            index = index + 1
                
            

        return status



        
