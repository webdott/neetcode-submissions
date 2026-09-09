class DSU:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.comp = n

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False

        self.comp -= 1
        pu, pv = [pu, pv] if pu >= pv else [pv, pu]
        
        self.size[pu] += self.size[pv]
        self.parents[pv] = pu
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        dsu = DSU(n)

        for r,c in edges:
            if not dsu.union(r, c):
                return [r,c]

        return edges[-1]

        

