class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = [0] * 9, [0] * 9, [0] * 9

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue
                    
                square_idx = (i // 3) * 3 + (j // 3)

                if 1 << int(val) - 1 & rows[i]:
                    return False
                
                if 1 << int(val) - 1 & cols[j]:
                    return False

                if 1 << int(val) - 1 & squares[square_idx]:
                    return False

                rows[i] |= 1 << int(val) - 1
                cols[j] |= 1 << int(val) - 1
                squares[square_idx] |= 1 << int(val) - 1

        return True