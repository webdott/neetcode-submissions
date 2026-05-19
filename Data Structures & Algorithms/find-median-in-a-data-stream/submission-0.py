class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.stream, num)

    def findMedian(self) -> float:
        mid_idx = math.floor(len(self.stream) / 2) + 1
        a = heapq.nlargest(mid_idx, self.stream)

        s = a[-1]

        if len(self.stream) % 2 == 0 and len(a) > 1:
            s += a[-2]
        else:
            s *= 2

        return (s / 2)