"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        current_start = 0
        current_end = 0
        for interval in intervals:
            if interval.start < current_end:
                return False
            else:
                current_start = interval.start
                current_end = interval.end

        return True
