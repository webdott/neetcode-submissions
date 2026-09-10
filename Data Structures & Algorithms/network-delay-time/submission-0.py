class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for r, c, t in times:
            adj[r].append((c, t))

         
        min_heap = []
        heapq.heappush(min_heap, (0, k))
        v = set()
        res = 0

        while min_heap:
            t, node = heapq.heappop(min_heap)

            if node in v:
                continue
            
            v.add(node)

            res = max(res, t)

            for d_n, d_t in adj[node]:
                if d_n in v:
                    continue

                heapq.heappush(min_heap, (t + d_t, d_n))

        return res if len(v) == n else -1