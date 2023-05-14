class TrieNode:
    def __init__(self, val):
        self.children = {}
        self.isEnd = False
        self.value = val


class Trie:
    def __init__(self):
        self.root = TrieNode(-1)

    def insert(self, word):
        curr = self.root
        for ch in word:
            if curr.isEnd:
                break
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]
        curr.isEnd = True

    def helper(self):
        def dfs(curr, val):
            if curr.isEnd:
                ans.append(val)
                return
            for child in curr.children:
                dfs(curr.children[child], val+'/'+child)

        ans = []
        dfs(self.root, "")
        return ans


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        for f in folder:
            path = f.split('/')[1:]
            root.insert(path)

        return root.helper()
