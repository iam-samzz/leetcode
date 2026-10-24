class Solution:
    
    def can_we_place(self,min_distance:int, n:int, arr:list, k: int):
        cow_placed = 1
        prev_pos = arr[0]
        for j in range(1 , n):
        
            # checking if the distance b.w current and prev cow placement has required min distance
            if arr[j] - prev_pos >= min_distance:
                cow_placed += 1
                prev_pos = arr[j]
            
            # once we reached by keeping k cows in the stalls, lets stop keeping extra cows..
            if cow_placed == k:
                
                # once we kept k cows, which means, this particular minimum distance is valid! 
                return  True
        return False
        
    
    def aggressiveCows(self, arr, k):
        # code here
        n = len(arr)
        
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
        
        max_arr = max(arr)
        min_arr = min(arr)
        
        #lower bound for min distanece = 1
        # upepr bound for minimum distance is  max_arr - min_arr , that is two cows places at two extreams.
        low = 1
        high = max_arr - min_arr
        
        while low <= high:
            
            mid = (low + high )//2
            
            if self.can_we_place(mid , n , arr, k):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
            
        return result
    
