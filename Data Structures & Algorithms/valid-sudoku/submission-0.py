class Solution:
    def getGrid(self, row: int, col: int) -> int:
        box_row = row // 3
        box_col = col // 3
        return box_row * 3 + box_col

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        grid_seen, row_seen, col_seen = [set() for i in range(n)], [set() for i in range(n)], [set() for i in range(n)]

        for row in range(n):
            for col in range(n):
                num = board[row][col]
                grid = self.getGrid(row, col)

                if num != "." and (num in grid_seen[grid] or num in row_seen[row] or num in col_seen[col]):
                    return False

                grid_seen[grid].add(num)
                row_seen[row].add(num)
                col_seen[col].add(num)
                

        return True

