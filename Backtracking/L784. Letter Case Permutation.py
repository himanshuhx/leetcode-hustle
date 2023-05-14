class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def solve(i, curr):
            if len(curr)==len(s):
                ans.append(curr)
                return
            for j in range(i,len(s)):
                if s[j].isalpha():
                    solve(j+1, curr+s[j].lower())
                    solve(j+1, curr+s[j].upper())
                else:
                    solve(j+1,curr+s[j])
        
        ans = []
        solve(0, "")
        return ans