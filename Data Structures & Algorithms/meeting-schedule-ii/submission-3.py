"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start_arr = []
        end_arr = []
        for interval in intervals:
            start_arr.append(interval.start)
        for interval in intervals:
            end_arr.append(interval.end)

        start_arr.sort()
        end_arr.sort()
        max_rooms = 0
        count_rooms = 0
        start_ptr = 0
        end_ptr = 0
        while start_ptr < len(start_arr):
            if start_arr[start_ptr] < end_arr[end_ptr]:
                count_rooms += 1
                start_ptr += 1
            else:
                count_rooms -= 1
                end_ptr += 1
            max_rooms = max(max_rooms , count_rooms)
        
        return max_rooms