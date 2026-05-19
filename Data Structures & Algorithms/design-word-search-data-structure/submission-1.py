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

    def searchInt(self, curr: TrieNode, word: str, idx: int) -> bool:
        if idx >= len(word):
            return curr.endOfWord
        
        char = word[idx]
        ord_idx = ord(char) - ord("a")

        if char == ".":
            should_advance = False

            for i in range(26):   
                if curr.children[i]:
                    should_advance = should_advance or self.searchInt(curr.children[i], word, idx + 1)

                    if should_advance:
                        return True 

            return False
        else:
            if not curr.children[ord_idx]:
                return False

            return self.searchInt(curr.children[ord_idx], word, idx + 1)


    def search(self, word: str) -> bool:
        return self.searchInt(self.tree, word, 0)
        
