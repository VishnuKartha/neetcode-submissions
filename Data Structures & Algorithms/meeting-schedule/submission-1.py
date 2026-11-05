"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if(len(intervals) <= 1):
            return True
        # sorted by start time
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        prev  = sorted_intervals[0]
        for curr in sorted_intervals[1:]:
            if curr.start < prev.end:
                return False
            prev = curr
        return True

