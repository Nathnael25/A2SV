class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        output = [intervals[0]]
        
        if len(intervals)<2:
            return intervals
        
        for start, end in intervals[1:]:
            if start > output[-1][1]:
                output.append([start,end])
            elif end > output[-1][1]:
                output[-1][1]=end
        return output