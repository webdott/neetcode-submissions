class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.size[pv] > self.size[pu]:
            pu, pv = pv, pu
        
        self.size[pu] += self.size[pv]
        self.parents[pv] = pu

        return True

class Solution:
    def minCostConnectPointsA(self, points: List[List[int]]) -> int:
        n = len(points)

        edges= []

        for i in range(n):
            for j in range(i + 1):
                a, b = points[i] 
                c, d = points[j]
                
                #  point a, point b, weight (distance)
                edges.append([i, j, abs(c - a) + abs(d - b)])

        edges.sort(key=lambda x: x[2])

        dsu = DSU(n)
        res, count = 0, 0

        for u, v, w in edges:
            if dsu.union(u, v):
                res += w
                count += 1
            
            if count == n - 1:
                break

        return res

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = [[] for _ in range(n)]

        for i in range(n):
            a, b = points[i] 
            for j in range(i + 1):
                c, d = points[j]
                
                adj[i].append([j, abs(c - a) + abs(d - b)])
                adj[j].append([i, abs(c - a) + abs(d - b)])


        min_heap = [(0, 0)]
        visited = set()
        res = 0

        while min_heap:
            if len(visited) == n:
                return res

            w, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            visited.add(v)
            res += w

            for nxt, n_w in adj[v]:
                if nxt not in visited:
                    heapq.heappush(min_heap, (n_w, nxt))

        return res



