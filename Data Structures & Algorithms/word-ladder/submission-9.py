class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        p = defaultdict(list)
        m = len(beginWord)
        n = len(wordList)

        wordList.append(beginWord)
        bInWord = False
        adj = defaultdict(set)

        for j,word in enumerate(wordList):
            if word == beginWord and j < n - 1:
                bInWord = True

            for i in range(m):
                sub = word[0:i] + "." +word[i+1:]

                for w in p[sub]:
                    adj[w].add(word)
                    adj[word].add(w)

                p[sub].append(word)

        if endWord not in adj:
            return 0

        v = set()
        r = {}
        def dfs(w, p):
            if w == beginWord:
                return 1

            if w in r:
                return r[w]

            if w in v:
                return math.inf

            v.add(w)

            val = math.inf

            for n_w in adj[w]:
                if n_w == p:
                    continue 

                val = min(1 + dfs(n_w, w), val)

            r[w] = val
            return val

        res = dfs(endWord, -1)
        return 0 if res >= math.inf else res