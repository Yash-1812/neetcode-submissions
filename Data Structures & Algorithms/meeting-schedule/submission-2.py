"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        for i in range(len(intervals) - 1):
            start_time = intervals[i].start
            end_time = intervals[i].end
            for j in range(i + 1 , len(intervals)):

                if start_time == intervals[j].start or end_time == intervals[j].end:
                    return False

                if start_time < intervals[j].start < end_time or start_time < intervals[j].end < end_time:
                    return False

        return True

