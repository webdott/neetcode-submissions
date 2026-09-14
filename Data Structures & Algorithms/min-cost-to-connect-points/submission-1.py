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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
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


