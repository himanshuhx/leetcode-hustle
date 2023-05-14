class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        def dfs(i, j, curr, word):
            if i < 0 or j < 0 or i == ROWS or j == COLS or (i, j) in visited or board[i][j] not in curr.children:
                return

            visited.add((i, j))
            word += board[i][j]
            curr = curr.children[board[i][j]]

            if curr.isEnd:
                res.add(word)

            dfs(i+1, j, curr, word)
            dfs(i-1, j, curr, word)
            dfs(i, j+1, curr, word)
            dfs(i, j-1, curr, word)

            visited.remove((i, j))

        res, visited = set(), set()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] in trie.children:
                    dfs(i, j, trie, '')

        return list(res)
