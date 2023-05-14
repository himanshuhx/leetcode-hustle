class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, root, word):
        curr = root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def dfs(self, curr, word):
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
            if curr.isEnd:
                return True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.suffix = ''
        for word in words:
            self.trie.insert(self.trie, word[::-1])

    def query(self, letter: str) -> bool:
        self.suffix = letter + self.suffix
        return self.trie.dfs(self.trie, self.suffix)
