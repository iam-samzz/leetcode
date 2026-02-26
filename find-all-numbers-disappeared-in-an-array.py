class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # input_index = [0,1,2,.. n-1]
        # so for each array, the range is 1 to len(Array)
            # these are the values that can be inside the arr
        
        #store the index in list.
        # check the index_list with the input list.
            #if any number missed, add to new list

        #excluding 0 from the index list.


        index_list = []
        op = []
        i = 0

        for index in range(1,len(nums)+1):
            index_list.append(index)
        


        for j in nums:
            if j not in index_list:
                op.append(j)
                
        print(j)
        return op
