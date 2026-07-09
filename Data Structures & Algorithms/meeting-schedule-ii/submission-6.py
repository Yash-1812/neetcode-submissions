"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        res = 0
        min_heap = []
        prevEnd = intervals[0].end
        for i in range(len(intervals)):
            start , end = intervals[i].start , intervals[i].end
            if min_heap and start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap , end)
        return len(min_heap)