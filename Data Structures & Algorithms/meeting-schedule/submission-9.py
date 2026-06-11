"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        arr = []
        for i in range(len(intervals)):
            arr.append((intervals[i].start , intervals[i].end))
        
        arr = sorted(arr)
        last = arr[0][1]
        for i in range(1 , len(arr)):
            if arr[i][0] < last:
                return False
            last = arr[i][1]
        return True