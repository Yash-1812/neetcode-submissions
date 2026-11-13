class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        latest = []
        prev_start , prev_end = intervals[0][0] , intervals[0][1]
        latest.append([prev_start , prev_end])
        for i in range(1 , len(intervals)):
            start , end = intervals[i]
            done = False
            for i in range(len(latest)):
                s , e = latest[i]
                if start > e:
                    latest[i][0] , latest[i][1] = start , end
                    done = True
                    break
            if not done:
                latest.append([start , end])
        return len(latest)