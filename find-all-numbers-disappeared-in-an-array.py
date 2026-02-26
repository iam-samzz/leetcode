class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        index_dict = {}  
        nums_dict = {}  
        op = []

       
        for index in range(1, len(nums)+1):
            index_dict[index] = True

        # Store numbers present in nums
        for number in nums:
            nums_dict[number] = True

        
        for num in index_dict:
            if num not in nums_dict:
                op.append(num)

        print(op)
        return op
