class Solution:
    def leastIntervalA(self, tasks: List[str], n: int) -> int:
        a = [0 for i in range(26)]

        for task in tasks:
            a[ord(task) - ord("A")] += 1

        h = []

        for c in a:
            if c > 0:
                h.append(c)

        res, lvl = 0, 0

        while h:
            res += max(0, (lvl * (n + 1)) - res)

            m = len(h)
            res += m
            k = []

            for i in range(m):
                x = h.pop()

                if x - 1 > 0:
                    k.append(x - 1)

            for l in k:
                h = k

            lvl += 1

        return res

    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        count.sort()
        maxf = count[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(maxf - 1, count[i])

        return max(0, idle) + len(tasks)