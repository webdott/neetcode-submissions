class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for c, r in prerequisites:
            adj[c].append(r)

        res = []
        s = set()
        t = set()
        v = {}

        def dfs(i):
            if len(adj[i]) == 0:
                if i not in s:
                    res.append(i)
                    s.add(i)

                return True

            if i in t:
                return False

            if i in v:
                return v[i]

            t.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            t.remove(i)

            if i not in s:
                res.append(i)
                s.add(i)

            v[i] = True
            return v[i]

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res