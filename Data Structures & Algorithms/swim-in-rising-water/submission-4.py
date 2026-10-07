class Solution:
    def swimInWaterA(self, grid: List[List[int]]) -> int:
        min_max = float('inf')
        rows = len(grid)
        cols = len(grid[0])
        dp = [[float('inf')] * cols for _ in range(rows)]

        def dfs(row, col, _max):
            nonlocal min_max

            if row >= rows or col >= cols or col < 0 or row < 0 or grid[row][col] == 'x' or dp[row][col] <= _max:
                return

            highest = max(grid[row][col], _max)
            if row == rows - 1 and col == cols - 1:
                min_max = min(min_max, highest)
                return

            dp[row][col] = _max
            temp = grid[row][col]
            grid[row][col] = 'x'
            
            for nxt_row, nxt_col in [[row - 1, col], [row, col + 1], [row + 1, col], [row, col - 1]]:
                dfs(nxt_row, nxt_col, highest)

            grid[row][col] = temp

        dfs(0, 0, grid[0][0])
        return min_max

    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def in_range(row, col):
            return 0 <= row < rows and 0 <= col < cols

        path = [(grid[0][0], 0, 0)]
        vst = set()

        while path:
            val, row, col = heapq.heappop(path)

            if row == rows - 1 and col == cols - 1:
                return val 

            if (row, col) in vst:
                continue

            vst.add((row, col))

            for nxt_row, nxt_col in [[row - 1, col], [row, col + 1], [row + 1, col], [row, col - 1]]:
                if in_range(nxt_row, nxt_col):
                    new_val = max(val, grid[nxt_row][nxt_col])
                    heapq.heappush(path, (new_val, nxt_row, nxt_col))
        
        return -1