class Solution:
    def isOverlapping(self, a, b, c, d) -> bool:
        return (b <= d and c <= b) or (d <= b and a <= d)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],x[1]))

        res = [intervals[0]]

        for a, b in intervals:
            c, d = res[-1]

            if self.isOverlapping(a, b, c, d):
                res[-1][0] = min(a, c)
                res[-1][1] = max(b, d)
            else:
                res.append([a, b])

        return res