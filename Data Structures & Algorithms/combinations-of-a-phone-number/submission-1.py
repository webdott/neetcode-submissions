class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res, n = [], len(digits)

        def dfs(idx: int, curr: List):
            if idx >= n:
                if len(curr) > 0:
                    res.append("".join(curr.copy()))
                return
            
            for x in self.digit_map[digits[idx]]:
                curr.append(x)
                dfs(idx + 1, curr)
                curr.pop()

        dfs(0, [])

        return res
        