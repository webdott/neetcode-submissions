class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
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