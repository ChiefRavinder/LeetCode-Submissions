class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort()
        result=0
        prevEnd=intervals[0][1]
        for start, end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
            else:
                result+=1
                prevEnd=min(end,prevEnd)
        return result
         