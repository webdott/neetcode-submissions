class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        os = set()

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in os or board[r][c] == "X":
                return

            os.add((r,c))

            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc

                dfs(rr, cc)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][cols - 1] == "O":
                dfs(r, cols-1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)

            if board[rows - 1][c] == "O":
                dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in os:
                    board[r][c] = "X"