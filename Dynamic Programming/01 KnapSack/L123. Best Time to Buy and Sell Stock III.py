class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(i, buy, count):
            if i>=len(prices):
                return 0
            if count<0:
                return 0
            key = (i,buy,count)
            if key in memo:
                return memo[key]
            if buy:
                memo[key] = max(solve(i+1,False,count-1)-prices[i],solve(i+1,True,count))
            else:
                memo[key] = max(solve(i+1,True,count)+prices[i],solve(i+1,False,count))
            return memo[key]
        
        memo = {}
        return solve(0,True,2)