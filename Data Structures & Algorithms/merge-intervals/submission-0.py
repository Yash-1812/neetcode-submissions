class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort()
        res = [intervals[0]]
        for i in range(1 , len(intervals)):
            temp = res.pop()
            if temp[1] < intervals[i][0]:
                res.append(temp)
                res.append(intervals[i])
            else:
                res.append([min(temp[0] , intervals[i][0]) , max(temp[1] , intervals[i][1])])
        
        return res