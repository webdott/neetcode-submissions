class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        fl = [[101, -1] for _ in range(27)]

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')

            fl[idx][0] = min(fl[idx][0], i)
            fl[idx][1] = max(fl[idx][1], i)

        ans = []
        i = 0

        while i < len(s):
            c = s[i]
            idx = ord(c) - ord('a')
            max_so_far = fl[idx][1]

            j = i + 1
            while j < max_so_far:
                k = ord(s[j]) - ord('a')
                max_so_far = max(max_so_far, fl[k][1])
                j += 1

            ans.append(max_so_far - i + 1)
            i = max_so_far + 1

        return ans

            


        