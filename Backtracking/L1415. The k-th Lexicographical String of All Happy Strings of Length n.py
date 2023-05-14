class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def solve(curr):
            nonlocal ans
            if len(ans)>=k:
                return
            if len(curr)==n:
                ans.append(''.join(curr))
                return
            for x in "abc":
                if curr and curr[-1]==x:
                    continue
                curr.append(x)
                solve(curr)
                curr.pop()
        
        ans = []
        solve([])
        return ans[k-1] if len(ans)>=k else ""