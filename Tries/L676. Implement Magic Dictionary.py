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

    def isPossible(self, root, word, count):
        if not word:
            return True if (root.isEnd and count == 0) else False
        for child in root.children:
            if child == word[0]:
                if self.isPossible(root.children[child], word[1:], count):
                    return True
            elif count == 1:
                if self.isPossible(root.children[child], word[1:], 0):
                    return True
        return False


class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.root.insert(self.root, word)

    def search(self, searchWord: str) -> bool:
        return self.root.isPossible(self.root, searchWord, 1)
