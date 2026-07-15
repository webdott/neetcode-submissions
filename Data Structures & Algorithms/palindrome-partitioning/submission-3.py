class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.si, self.ans = s, []

        self.bt(0, [])

        return self.ans

    def is_palindrome(self, li: List[str]) -> bool:
        l, r = 0, len(li) - 1

        while l < r:
            if li[l] != li[r]:
                return False

            l += 1
            r -= 1

        return True
    
    def bt(self, i: int, curr: List[List[str]]):
        if i >= len(self.si):
            f_a = []
            
            for poss_palindrome in curr:
                if not self.is_palindrome(poss_palindrome):
                    return

                f_a.append("".join(poss_palindrome))

            self.ans.append(f_a)
            return

        curr.append([self.si[i]])
        self.bt(i + 1, curr)
        curr.pop()

        if len(curr) == 0 or len(curr[-1]) == 0:
            return

        curr[-1].append(self.si[i])
        self.bt(i + 1, curr)
        curr[-1].pop()

