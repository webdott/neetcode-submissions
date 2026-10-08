class Solution:
    def foreignDictionary(self, words: List[str]) -> str:  
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}

        n = len(words)
        for i in range(n - 2, -1, -1):
            l, r = words[i], words[i + 1]
            m, n = len(l), len(r)

            if m > n and l[:n] == r[:n]:
                return ""

            for j in range(min(m, n)):
                if l[j] != r[j]:
                    if l[j] in adj[r[j]]:
                        return ""
                    if r[j] in adj[l[j]]:
                        break

                    adj[l[j]].add(r[j])
                    indegree[r[j]] += 1
                    break

        q = deque([])

        for c in adj:
            if indegree[c] == 0:
                q.append(c)

        res = []
        while q:
            node = q.popleft()
            res.append(node)  
            for nxt in adj[node]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)

        if len(res) != len(indegree):
            return ""

        return "".join(res)
