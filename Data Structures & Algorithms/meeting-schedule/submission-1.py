"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
def overlap(int1: Interval, int2: Interval) -> bool:
    return not (int1.start >= int2.end or int2.start >= int1.end)

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))
        for i in range(1, len(intervals)):
            if overlap(intervals[i], intervals[i-1]): return False
        return True
