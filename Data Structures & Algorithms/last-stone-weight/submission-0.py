class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-num for num in stones]

        heapq.heapify(s)

        while len(s) > 1:
            # print(s)
            x, y = -heapq.heappop(s), -heapq.heappop(s)

            diff = abs(x - y)

            if diff > 0:
                heapq.heappush(s, -diff) 

        return -s[0] if len(s) == 1 else 0