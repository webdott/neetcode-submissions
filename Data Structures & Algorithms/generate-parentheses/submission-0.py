class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        self.backtrack(n * 2, [], 0, 0)

        return self.ans
    
    def backtrack(self, n:int, curr: List[str], front: int, back: int):
        if back > front:
            return;

        if front + back == n:
            if front == back:
                self.ans.append("".join(curr[:]))
                
            return

        curr.append("(")
        self.backtrack(n, curr, front + 1, back)
        curr.pop()

        curr.append(")")
        self.backtrack(n, curr, front, back + 1)
        curr.pop()
