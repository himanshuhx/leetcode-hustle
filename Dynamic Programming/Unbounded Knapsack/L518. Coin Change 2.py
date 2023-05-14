class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def solve(n, amount):
            if amount==0:
                return 1
            key = (n,amount)
            if key in memo:
                return memo[key]
            if n<0 or amount<0:
                return 0
            if coins[n]<=amount:
                memo[key] = solve(n,amount-coins[n]) + solve(n-1,amount)
            else:
                memo[key] = solve(n-1,amount)
            return memo[key]
        
        memo = {}
        res = solve(len(coins)-1,amount)
        return -1 if res==float("inf") else res