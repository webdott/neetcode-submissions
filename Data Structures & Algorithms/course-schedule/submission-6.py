class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        s, v = set(), {}

        for r, c in prerequisites:
            if r == c:
                return False

            adj[r].add(c)
            
        def dfs(i) -> bool:
            if i in v:
                return True

            if len(adj[i]) == 0:
                return True

            if i in s:
                return False

            s.add(i)

            for x in adj[i]:
                if x in s or not dfs(x):
                    return False

            s.remove(i)

            v[i] = True
            return True

        for x in range(numCourses):
            if not dfs(x):
                return False

        return True
        