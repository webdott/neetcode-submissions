"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def is_overlapping(self, a, b, c, d):
        return (b <= d and c < b) or (d <= b and a < d)
    def minMeetingRoomsP(self, intervals: List[Interval]) -> int:
        res = []

        intervals.sort(key=lambda x: (x.start, x.end))

        for interval in intervals:
            if not res:
                res.append(interval)
                continue

            a, b = interval.start, interval.end
            i = 0

            while i < len(res) and self.is_overlapping(res[i].start, res[i].end, a, b):
                i += 1

            if i >= len(res):
                res.append(interval)
            else:
                res[i].start = min(res[i].start, interval.start)
                res[i].end = max(res[i].end, interval.end)

        return len(res)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res, count = 0, 0

        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        s, e = 0, 0

        while s < len(start) or e < len(end):
            ss = math.inf if s >= len(start) else start[s]
            ee = math.inf if e >= len(end) else end[e]

            if ss < ee:
                count += 1
                s += 1
            elif ss > ee:
                res = max(res, count)
                count -= 1
                e += 1
            else:
                s += 1
                e += 1


        return res
