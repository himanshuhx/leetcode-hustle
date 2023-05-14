class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = ''


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        count = 0
        flag = False
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True
        curr.word = word

    def bfs(self):
        queue = collections.deque()
        queue.append(self.root)
        res = ''
        while queue:
            node = queue.popleft()
            for c in node.children.values():
                if c.isEnd:
                    queue.append(c)
                    if len(c.word) > len(res) or c.word < res:
                        res = c.word
        return res


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        print(words)
        root = Trie()
        for word in words:
            root.insert(word)

        return root.bfs()
