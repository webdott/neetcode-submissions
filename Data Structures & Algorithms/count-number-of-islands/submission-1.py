class Solution:
    def getNeighbors(self, row: int, col: int) -> List(Tuple):
        return [
            (row - 1, col),
            (row, col + 1),
            (row + 1, col),
            (row, col - 1)
        ]

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def isIsland(row: int, col: int) -> bool:
            if row >= n or col >= m or row < 0 or col < 0 or grid[row][col] == "0":
                return False

            grid[row][col] = "0"

            nxt = self.getNeighbors(row, col)

            for r, c in nxt:
                isIsland(r, c)

            return True

        res = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "0":
                    continue

                if isIsland(r, c):
                    res += 1

        return res
