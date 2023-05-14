class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 10
        res = [9]
        for i in range(1,n-1):
            res.append(res[-1]*(9-i))
        return 10+(9*sum(res))