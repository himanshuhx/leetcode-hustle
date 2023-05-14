class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(i, candidate):
            if i == len(s):
                res.append(candidate[:].strip())
                return

            for j in range(i, len(s)):
                curr_candidate = s[i:j+1]
                if curr_candidate in words:
                    dfs(j+1, candidate+" "+curr_candidate)

        words = set(wordDict)
        res = []
        dfs(0, '')
        return res
