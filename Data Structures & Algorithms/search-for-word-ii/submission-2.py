class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.tree = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.tree
        
        for char in word:
            idx = ord(char) - ord("a")

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        curr.endOfWord = True

    def getNeighbours(self, row, col) -> [(int, int)]:
        return [
            (row - 1, col),
            (row, col + 1),
            (row + 1, col),
            (row, col - 1),
        ]

    def search(self, curr, board, row, col, rows, cols, seen, words, res) -> bool:
        if not curr:
            return 

        if curr.endOfWord:
            res.add("".join(words))

        key = str(row) + "-" + str(col)
        if row >= rows or row < 0 or col >= cols or col < 0 or key in seen:
            return
        

        char = board[row][col]
        ord_idx = ord(char) - ord("a")

        if not curr.children[ord_idx]:
            return

        seen.add(key)
        words.append(char)

        neighbours = self.getNeighbours(row, col)

        for neighbour in neighbours:
            next_row, next_col = neighbour

            self.search(curr.children[ord_idx], board, next_row, next_col, rows, cols, seen, words, res)

        seen.remove(key)
        words.pop()
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dictionary = WordDictionary()

        for word in words:
            dictionary.addWord(word)

        res = set()
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                i_res = set()

                dictionary.search(dictionary.tree, board, row, col, rows, cols, set(), [], i_res)

                for word in i_res:
                    res.add(word)

        return list(res)