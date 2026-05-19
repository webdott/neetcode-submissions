class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, n = 0, 0, len(s)
        res = 0

        _set = defaultdict(int)

        while r <= n:
            if r == n or (s[r] in _set and _set[s[r]] >= l):
                res = max(res, r - l)

                if r < n:
                    l = _set[s[r]] + 1

            if r < n:
                _set[s[r]] = r

            r += 1

        return res