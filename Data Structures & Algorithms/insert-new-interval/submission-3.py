class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start , end = newInterval[0] , newInterval[1]
        result = []
        for i in range(0 , len(intervals)):
            if start <= intervals[i][1] and end >= intervals[i][0]:
                start = min(start , intervals[i][0])
                end = max(end , intervals[i][1])
            elif start >= intervals[i][1]:
                result.append(intervals[i].copy())
            elif end <= intervals[i][1]:
                result.append([start , end].copy())
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start , end].copy())
        return result