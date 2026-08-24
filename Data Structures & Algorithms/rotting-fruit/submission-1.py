class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        [
            [1,0,1],
            [0,2,0],
            [1,0,1]
        ]

        q = deque()
        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        total_fruits = affected = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    affected += 1

                if grid[r][c] > 0:
                    total_fruits += 1

        minute = 0

        while q:
            l = len(q)

            for _ in range(l):
                r, c = q.popleft()

                for dr, dc in DIRECTIONS:
                    rr, cc = r + dr, c + dc

                    if rr not in range(rows) or cc not in range(cols) or grid[rr][cc] != 1:
                        print(rr, cc)
                        continue

                    affected += 1
                    grid[rr][cc] = 2
                    q.append((rr, cc))

            minute += 1

        print(minute, affected, total_fruits)
        return max(0, minute - 1) if affected == total_fruits else -1