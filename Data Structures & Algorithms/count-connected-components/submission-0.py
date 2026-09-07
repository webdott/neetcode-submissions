class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
        self.comp = n

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return

        self.comp -= 1

        if self.size[pv] > self.size[pu]:
            pu, pv = [pv, pu]

        self.parents[pv] = pu
        self.size[pu] += self.size[pv]

    def comps(self):
        return self.comp

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        dsu = DSU(n)

        for r,c in edges:
            adj[r].append(c)
            adj[c].append(r)

        for i in range(n):
            for j in adj[i]:
                dsu.union(i, j)

        return dsu.comps()

        