class TrieNode:
    def __init__(self, data):
        self.children = {}
        self.isEnd = True
        self.data = data


class Trie:
    def __init__(self):
        self.root = TrieNode('#')

    def insert(self, word, val):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(val)
            else:
                curr.children[ch].data += val
            curr = curr.children[ch]
        curr.isEnd = True

    def override(self, word, val, old_val):
        curr = self.root
        for ch in word:
            curr.children[ch].data += (val - old_val)
            curr = curr.children[ch]

    def getSum(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]

        return curr.data


class MapSum:

    def __init__(self):
        self.present = {}
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        if key in self.present:
            self.trie.override(key, val, self.present[key])
        else:
            self.trie.insert(key, val)
        self.present[key] = val

    def sum(self, prefix: str) -> int:
        return self.trie.getSum(prefix)
