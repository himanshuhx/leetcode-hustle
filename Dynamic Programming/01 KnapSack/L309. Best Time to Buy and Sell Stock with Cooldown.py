class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def solve(i, turnToBuy):
            if i>len(prices)-1:
                return 0
            key = (i, turnToBuy)
            if key in memo:
                return memo[key]
            profit = 0
            if turnToBuy:
                bought = -prices[i] + solve(i+1,False)
                notBought = solve(i+1,True)
                profit = max(bought, notBought)
            else:
                sold = solve(i+2,True) + prices[i]
                notSold = solve(i+1,False)
                profit = max(sold, notSold)
            memo[key] = profit
            return memo[key]
        
        memo = {}
        return solve(0,True)
        