class Solution:
    def islandsAndTreasureDFS(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(r: int, c: int, num: int):
            if grid[r][c] == -1 or (grid[r][c] == 0 and num > 0):
                return

            for dr, dc in DIRECTIONS:
                rr, cc = r + dr, c + dc

                if rr in range(rows) and cc in range(cols):
                    if num + 1 < grid[rr][cc]:
                        grid[rr][cc] = num + 1

                        dfs(rr, cc, num + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r, c, 0)

    def islandsAndTreasureSingleBFS(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def bfs(row, col):
            q = deque([(row, col, 0)])
            s = set()
            s.add((row,col))

            while q:
                r, c, n = q.popleft()

                for dr, dc in DIRECTIONS:
                    rr, cc = r + dr, c + dc

                    if rr in range(rows) and cc in range(cols) and (rr, cc) not in s and grid[rr][cc] != -1 and grid[rr][cc] != 0:
                        grid[rr][cc] = min(grid[rr][cc], n + 1)
                        s.add((rr, cc)) 
                        q.append((rr, cc, n + 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r, c)

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        q = deque()
        s = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    s.add((r, c))

        def bfs():
            while q:
                l = len(q)

                for _ in range(l):
                    r, c, n = q.popleft()

                    for dr, dc in DIRECTIONS:
                        rr, cc = r + dr, c + dc

                        if rr in range(rows) and cc in range(cols) and (rr, cc) not in s and grid[rr][cc] != -1:
                            grid[rr][cc] = min(grid[rr][cc], n + 1)
                            s.add((rr, cc)) 
                            q.append((rr, cc, n + 1))

        bfs()
