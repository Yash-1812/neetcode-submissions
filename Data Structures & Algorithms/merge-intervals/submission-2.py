class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start , end = intervals[0][0] , intervals[0][1]
        for i in range(1 , len(intervals)):
            if start <= intervals[i][1] and end >= intervals[i][0]:
                start = min(start , intervals[i][0])
                end = max(end , intervals[i][1])
            else:
                res.append([start , end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start , end])
        return res