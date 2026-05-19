class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        if n > m:
            return ""


        s1, s2 = {}, {}

        for char in t:
            s1[char] = 1 + s1.get(char, 0)

        curr_match = 0
 
        l, res, _min = 0, "", float('inf')
        for r in range(m):
            char = s[r]

            if char in s1:
                s2[char] = 1 + s2.get(char, 0)
                if s2[char] <= s1[char]:
                    curr_match += 1

            while l < r and s2.get(s[l], 1002) > s1.get(s[l], 1001):
                if s[l] in s2:
                    s2[s[l]] -= 1
                    
                    if s2[char] < s1[char]:
                        curr_match -= 1

                l += 1

            if curr_match == n and (r - l + 1) < _min:
                _min = r - l + 1
                res = s[l : r + 1]

        return res
            


        