class PrefixTree:
    def __init__(self):
        self.tree = {'children': {}}

    def insert(self, word: str) -> None:
        curr = self.tree
        
        for char in word:
            if char not in curr['children']:
                curr['children'][char] = {'children': {}}

            curr = curr['children'][char]

        curr['end'] = True
        
    def search(self, word: str) -> bool:
        curr = self.tree

        for char in word:
            if char not in curr['children']:
                return False

            curr = curr['children'][char]

        return 'end' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree

        for char in prefix:
            if char not in curr['children']:
                return False

            curr = curr['children'][char]

        return True
        