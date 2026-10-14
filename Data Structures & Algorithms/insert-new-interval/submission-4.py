class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval.copy())
        intervals.sort()
        res = []
        start , end = intervals[0][0] , intervals[0][1]
        for i in range(1 , len(intervals)):
            s , e = intervals[i][0] , intervals[i][1]
            if s <= end:
                start = min(start , s)
                end = max(end , e)
            else:
                res.append([start , end].copy())
                start = s
                end = e
        res.append([start , end].copy())
        return res