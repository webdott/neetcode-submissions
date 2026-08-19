class Solution:
    def checkValidString(self, s: str) -> bool:
        l_s, s_s = [], []

        for i, c in enumerate(s):
            if c == "*":
                s_s.append(i)
            elif c == "(":
                l_s.append(i)
            else:
                if len(l_s):
                    l_s.pop()
                elif len(s_s):
                    s_s.pop()
                else:
                    return False

        while len(l_s) > 0 and len(l_s) <= len(s_s):
            if l_s[-1] > s_s[-1]:
                return False

            l_s.pop()
            s_s.pop()

        return len(l_s) == 0