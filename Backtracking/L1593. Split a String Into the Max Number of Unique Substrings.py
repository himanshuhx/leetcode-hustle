class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(start):
            count =0
            for j in range(start, len(s)):
                if s[start:j+1] in seen:
                    continue
                ss = s[start:j+1]
                seen.add(ss)
                count = max(count, 1 + dfs(j+1))               
                seen.remove(ss)
            return count
        
        seen = set()
        count = dfs(0)
        return count