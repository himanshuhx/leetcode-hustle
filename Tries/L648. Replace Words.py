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

    def helper(self, sentence):
        res = ""
        sentence = list(sentence.split(" "))
        for word in sentence:
            shortestSuccessor = ""
            curr = self.root
            flag = True
            for ch in word:
                if ch not in curr.children:
                    flag = False
                    res += word+" "
                    break
                if ch in curr.children and curr.children[ch].isEnd == True:
                    flag = False
                    shortestSuccessor += ch
                    res += (shortestSuccessor + " ")
                    break
                shortestSuccessor += ch
                curr = curr.children[ch]
            if flag:
                res += word+" "
        return res.strip()


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:
            root.insert(word)

        return root.helper(sentence)
