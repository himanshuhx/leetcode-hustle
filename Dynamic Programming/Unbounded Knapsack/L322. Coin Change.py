class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(n, amount):
            if amount==0:
                return 0
            if n<0 or amount<0:
                return float("inf")
            if coins[n]<=amount:
                return min( 1+solve(n,amount-coins[n]), solve(n-1,amount))
            else:
                return solve(n-1,amount)
        res = solve(len(coins)-1,amount)
        return -1 if res==float("inf") else res