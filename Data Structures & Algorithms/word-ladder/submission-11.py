class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        p = defaultdict(list)
        m, n = len(beginWord), len(wordList)

        wordList.append(beginWord)
        bInWord = False
        adj = defaultdict(list)

        for j,word in enumerate(wordList):
            if word == beginWord and j < n:
                bInWord = True

            if bInWord and j == n:
                continue

            for i in range(m):
                sub = word[0:i] + "." + word[i+1:]

                for w in p[sub]:
                    adj[w].append(word)
                    adj[word].append(w)

                p[sub].append(word)

        if endWord not in adj:
            return 0

        q = deque()
        v = set()
        q.append([endWord, 1])

        while q:
            node, step = q.popleft()
            v.add(node)

            if node == beginWord:
                return step

            for n_w in adj[node]:
                if n_w in v:
                    continue

                q.append([n_w, step + 1])

        return 0