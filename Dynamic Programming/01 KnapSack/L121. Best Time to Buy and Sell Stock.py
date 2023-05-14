class Solution:
    def maxProfit(prices: List[int]) -> int:
        start = float("inf")
        profit, end = 0, start
        for price in prices:
            start = min(start,price)
            end = max(start,price)
            profit = max(profit,end-start)
        return profit

