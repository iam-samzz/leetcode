'''
    Brute force method

'''

class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        
        
        # eg : [1 , 2, 4 ,8 , 9]
        '''
            number line representation
            ----------------------------------------
            '1' , '2' , 3 , '4', 5 , 6 , 7 , '8', 9' 
        '''
        
        '''
        We sort so we can move sequentially from left to right along a straight line.

        If the stalls are in a random order, we would jump back and 
        forth across the number line, making it impossible to correctly calculate 
        distances between adjacent cows.
        '''
        
        result = None
        
        arr.sort()
        
        # the ranges of minimum distance for the stalls  is from 1 to  (distance b.w 1st element and last element)
        # i.e [1, max(arr) - min(arr)] inclusive range.
        
        max_arr = arr[-1]
        min_arr = arr[0]
        
        #lower bound for min distanece = 1
        # upepr bound for minimum distance is  max_arr - min_arr , that is two cows places at two extreams.
        for i in range(1 , max_arr - min_arr + 1):
            
            # for every min distance, check if we can keep k cows
            
            # if yes, then change result
            
            # if no , then do nothing
            
            is_min_distance_valid = False
            
            # 1st cow is 1st placed in all combinations..in 1st pos
            cow_placed = 1
            prev_pos = arr[0]
            
            # starting from second element
            for j in range(1 , len(arr)):
                
                # checking if the distance b.w current and prev cow placement has required min distance
                if arr[j] - prev_pos >= i:
                    cow_placed += 1
                    prev_pos = arr[j]
                
                # once we reached by keeping k cows in the stalls, lets stop keeping extra cows..
                if cow_placed == k:
                    
                    # once we kept k cows, which means, this particular minimum distance is valid! 
                    is_min_distance_valid = True
                    break
            
            
            if is_min_distance_valid:
                result = i
            else:
                break
        return result
