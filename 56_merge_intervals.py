class Solution(object):
    def merge(self, intervals):
        intervals.sort(key =lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:] :
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end,end)
            else:
                output.append([start,end])    
        return output        
# Time complexity O(n log n)