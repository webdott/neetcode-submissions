class Solution:
    def findCheapestPriceDFS(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for s, d, p in flights:
            adj[s].append((d, p))

        vst = {}
        ans = float('inf')

        def dfs(n, pr, st): 
            nonlocal ans

            a, b = vst.get(n, (0, float('inf')))      
            if st < 0 or (st <= a and pr >= b):
                return

            if n == dst:
                ans = min(ans, pr)
                return

            vst[n] = (st, pr)

            for nxt, p in adj[n]:
                dfs(nxt, pr + p, st - 1)

        dfs(src, 0, k + 1)

        return -1 if ans == float('inf') else ans

    def findCheapestPriceDjikstra(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = defaultdict(list)
        dist = [[INF] * (k + 2) for _ in range(n)]

        for s, d, p in flights:
            adj[s].append((d, p))

        minHeap = [(0, src, -1)]
        dist[src][0] = 0

        while len(minHeap):
            cst, node, stp = heapq.heappop(minHeap)

            if dst == node: 
                return cst
            if stp == k or dist[node][stp + 1] < cst: 
                continue

            for nxt, pr in adj[node]:
                nxt_cst = cst + pr
                nxt_stp = stp + 1

                if dist[nxt][nxt_stp + 1] > nxt_cst:
                    dist[nxt][nxt_stp + 1] = nxt_cst
                    heapq.heappush(minHeap, (nxt_cst, nxt, nxt_stp))

        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[src] = 0

        for _ in range(k + 1):
            tmp_p = dist.copy()

            for s, d, p in flights:
                if dist[s] == float('inf'): continue

                if tmp_p[d] > dist[s] + p:
                    tmp_p[d] = dist[s] + p

            dist = tmp_p

        return -1 if dist[dst] == float('inf') else dist[dst]


            
