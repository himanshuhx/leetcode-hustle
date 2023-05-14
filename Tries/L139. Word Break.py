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

    def search(self, root, word):
        curr = root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return curr.isEnd


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = TrieNode()
        n = len(s)

        for word in wordDict:
            trie.insert(trie, word)

        dp = [False for i in range(n+1)]
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and trie.search(trie, s[j:i]):
                    dp[i] = True
                    break

        return dp[-1]
