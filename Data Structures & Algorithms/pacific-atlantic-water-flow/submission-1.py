class Solution:
    def pacificAtlanticBFS(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in DIRECTIONS:
                    rr, cc = r + dr, c + dc
                    if (0 <= rr < rows and 0 <= cc < cols
                            and (rr, cc) not in visited
                            and heights[rr][cc] >= heights[r][c]):
                        visited.add((rr, cc))
                        queue.append((rr, cc))
            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r, c in pacific & atlantic]
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in DIRECTIONS:
                rr, cc = r + dr, c + dc
                if (0 <= rr < rows and 0 <= cc < cols
                        and (rr, cc) not in visited
                        and heights[rr][cc] >= heights[r][c]):
                    dfs(rr, cc, visited)

        pacific, atlantic = set(), set()

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        return [[r, c] for r, c in pacific & atlantic]