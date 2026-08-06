"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prevEnd = -math.inf
        intervals.sort(key=lambda x: (x.start, x.end))

        for interval in intervals:
            currStart, currEnd = interval.start, interval.end

            if currStart < prevEnd:
                return False

            prevEnd = max(prevEnd, currEnd)

        return True
