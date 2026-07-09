class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start , end = intervals[0][0] , intervals[0][1]
        result = []
        for i in range(1 , len(intervals)):
            if start <= intervals[i][1] and end >= intervals[i][0]:
                start = min(start , intervals[i][0])
                end = max(end , intervals[i][1])
            elif end < intervals[i][0]:
                result.append([start , end].copy())
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start , end].copy())
        return result