class Solution:
    def is_overlap(self, a, b, c, d) -> bool:
        return c < b

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], x[1]))

        li, idx, res = [intervals[0]], 1, 0

        while idx < len(intervals):
            a, b = li[-1]
            c, d, = intervals[idx]

            if self.is_overlap(a, b, c, d):
                res += 1
                if d < b:
                    li[-1] = intervals[idx]
            else:
                li.append(intervals[idx])

            idx += 1

        return res