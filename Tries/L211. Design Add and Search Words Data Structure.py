class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, root, word):
        curr = root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def addWord(self, word: str) -> None:
        self.insert(self.root, word)

    def search(self, word: str) -> bool:
        self.found = False
        root = self.root
        self.dfs(root, word)
        return self.found

    def dfs(self, curr, word):
        if not word:
            if curr.isEnd:
                self.found = True
            return

        if word[0] == '.':
            for child in curr.children.values():
                self.dfs(child, word[1:])
        else:
            if word[0] not in curr.children:
                return
            curr = curr.children[word[0]]
            self.dfs(curr, word[1:])
