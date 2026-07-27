class Solution:
    def isInvalid(self, row, col, n) -> bool:
        init = len(self.check['rows'][row]) > 0 or len(self.check['cols'][col]) > 0

        if init:
            return True

        e, f = row - 1, col + 1
        g, h = row - 1, col - 1
        
        while (e >= 0 and f < n) or (g >= 0 and h >= 0):
            if g >= 0 and h >= 0:
                if self.board[g][h] == "Q":
                    return True  
                g -= 1
                h -= 1

            if e >= 0 and f < n:
                if self.board[e][f] == "Q":
                    return True
                e -= 1
                f += 1

        return False
                

    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = cols = n
        ans = []

        self.board = [["." for col in range(cols)] for row in range(rows)]
        self.check = {'rows':defaultdict(set), 'cols':defaultdict(set)}

        def backtrack(row=-1, col=-1): 
            if row >= rows:
                ans.append(["".join(r) for r in self.board])
                return

            for coll in range(cols):
                if row + 1 < rows:
                    if self.isInvalid(row + 1, coll, n):
                        continue

                    self.board[row + 1][coll] = "Q"
                    self.check['rows'][row + 1].add((row + 1, coll))
                    self.check['cols'][coll].add((row + 1, coll))

                    backtrack(row + 1, coll)

                    self.board[row + 1][coll] = "."
                    self.check['rows'][row + 1].remove((row + 1, coll))
                    self.check['cols'][coll].remove((row + 1, coll))
                else:
                    backtrack(row + 1, coll)
                    break

        backtrack()

        return ans
