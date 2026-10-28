class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        

        # maximum weight capasity --> sum (weights) --> result in deliver within 1 day
        #  we need to find the  minium  weight capasity so that ->it results in delivery <= days or witinn days

        max_weight_capacity = sum(weights)

        low = max(weights) # max(weight) is the minimum that  need to be carried by the ship...
        high = max_weight_capacity  # maximum of max weight

        min_days = None

        while low <= high:
            mid = (low + high) // 2

            #mid is the current weight capacity 
            # now lets find the number of days it takes


            days_taken = 1
            current_weight = 0
            for num in weights:
                if num + current_weight > mid:
                    days_taken += 1
                    current_weight = num
                else:
                    current_weight += num
            

            if days_taken <= days:
                min_days = mid
                high = mid - 1
            else:
                low = mid + 1
        return min_days

        