class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def helper(self, queries):
        res = []
        for query in queries:
            curr = self.root
            flag = True
            for ch in query:
                if ch not in curr.children and ch.isupper():
                    flag = False
                    res.append(False)
                    break
                elif ch in curr.children:
                    curr = curr.children[ch]

            if flag:
                res.append(curr.isEnd)

        return res


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        root = Trie()

        root.insert(pattern)

        return root.helper(queries)
