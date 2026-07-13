class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows, self.cols = len(board), len(board[0])

        for row in range(self.rows):
            for col in range(self.cols):
                if self.dfs(board, word, row, col, 1):
                    return True

        return False

    def getNextPos(self, row: int, col: int) -> List[List[int]]:
        return [
            [row - 1, col],
            [row, col + 1],
            [row + 1, col],
            [row, col - 1]
        ]
        
    def dfs(self, board: List[List[str]], word: str, row:int, col: int, word_len: int) -> bool:
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or board[row][col] == "." or board[row][col] != word[word_len - 1]:
            return False


        if word_len == len(word):
            if board[row][col] == word[-1]:
                return True

            return False

        temp = board[row][col]
        board[row][col] = "."

        found = False

        for next_row, next_col in self.getNextPos(row, col):
            found = found or self.dfs(board, word, next_row, next_col, word_len + 1)

        board[row][col] = temp

        return found

        

        