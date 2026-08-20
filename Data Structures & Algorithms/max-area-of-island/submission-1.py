class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u, v) -> (int, bool):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return (self.size[pu], False)
        elif pu >= pv:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
            return (self.size[pu], True)
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
            return (self.size[pv], True)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dsu = DSU(rows * cols)

        max_area = 0

        def idx(r, c) -> int:
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, 1)

                    for dr, dc in directions:
                        rr, cc = r + dr, c + dc

                        if rr < 0 or cc < 0 or rr >= rows or cc >= cols or grid[rr][cc] == 0:
                            continue

                        cur_area, _ = dsu.union(idx(r, c), idx(rr, cc))
                        max_area = max(max_area, cur_area)

        return max_area

