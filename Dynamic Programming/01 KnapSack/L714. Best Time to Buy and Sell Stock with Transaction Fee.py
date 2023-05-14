class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def solve(i,buy):
            if i>=len(prices):
                return 0
            key = (i,buy)
            if key in memo:
                return memo[key]
            if buy:
                memo[key] = max(solve(i+1,False)-prices[i],solve(i+1,True))
            else:
                memo[key] = max(solve(i+1,True)+prices[i]-fee,solve(i+1,False))
            return memo[key]
        
        memo = {}
        return solve(0,True)