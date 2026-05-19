class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m_h = []

        for i in range(len(points)):
            p = points[i]

            heapq.heappush(m_h, ((p[0]**2) + (p[1]**2), i))

        res = []

        while k > 0:
            p, i = heapq.heappop(m_h)
            res.append(points[i])
            k -= 1

        return res