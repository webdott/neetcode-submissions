class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        q = [[query, i] for i, query in enumerate(queries)]
        q.sort(key=lambda x: x[0])
        intervals.sort(key=lambda x: (x[0], x[1]))

        m_h = []
        i = 0

        for query, j in q:
            m = -1

            while i < len(intervals) and intervals[i][0] <= query:
                a, b = intervals[i]
                heapq.heappush(m_h, (b - a + 1, b))
                i += 1

            while m_h and m_h[0][1] < query:
                heapq.heappop(m_h)

            if m_h and m_h[0][1] >= query:
                m = m_h[0][0]

            res[j] = m

        return res