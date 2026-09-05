class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        s = set()

        def dfs(i, prev):
            if i in s:
                return False

            if len(adj[i]) == 0:
                return True

            s.add(i)

            for j in adj[i]:
                if j == prev:
                    continue

                if not dfs(j, i):
                    return False
                
            return True

        if not dfs(0, None):
            return False
    
        return len(edges) == 0 or len(s) == n