class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key = lambda x : x[0])

        output = [intervals[0]]

        for interval in intervals[1:]:
            last_interval_end = output[-1][1]
            current_start = interval[0]
            current_end = interval[1]

            if current_start <= last_interval_end:
                output[-1][1] = max(last_interval_end,current_end)
            else:
                output.append([interval[0],interval[1]])
        return output
            
            
