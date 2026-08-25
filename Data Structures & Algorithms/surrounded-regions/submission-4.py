class DSU:
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols
        n = rows * cols
        self.parents = [i for i in range(n)]
        self.size = [1] * (n)

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def isEdge(self, n) -> int:
        r, c = n // self.cols, n % self.cols

        return r == 0 or r == self.rows - 1 or c == 0 or c == self.cols - 1

    def ab(self, pu, pv):
        self.parents[pv] = pu
        self.size[pu] += self.size[pv]

    def ba(self, pu, pv):
        self.parents[pu] = pv
        self.size[pv] += self.size[pu]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if self.isEdge(pu):
            self.ab(pu, pv)
        elif self.isEdge(pv):
            self.ba(pu, pv)
        elif self.size[pu] >= self.size[pv]:
            self.ab(pu, pv)
        else:
            self.ba(pu, pv)

    def p(self):
        return self.parents

# [
#     ["X","O","X","O","X","O"],
#     ["O","X","O","X","O","X"],
#     ["X","O","X","O","X","O"],
#     ["O","X","O","X","O","X"]
# ]

# [   ANS                               MINE
#     ["X","O","X","O","X","O"],        ["X","O","X","O","X","X"]
#     ["O","X","X","X","X","X"],        ["X","X","O","X","X","X"]
#     ["X","X","X","X","X","O"],        ["X","O","X","O","X","X"]
#     ["O","X","O","X","O","X"]         ["X","X","O","X","X","X"]
# ]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def idx(r, c) -> int:
            return r * cols + c

        def isEdge(n) -> int:
            r, c = n // cols, n % cols

            return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

        dsu = DSU(rows, cols)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    for dr, dc in DIRS:
                        rr, cc = r + dr, c + dc

                        if rr in range(rows) and cc in range(cols) and board[rr][cc] == "O":
                            dsu.union(idx(r, c), idx(rr, cc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not isEdge(dsu.find(idx(r, c))):
                    board[r][c] = "X"


    def solveDFS(self, board: List[List[str]]) -> None:
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