class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def feasible(num):
            currCnt = 0
            currRow, currCol = m-1, 0
            while currRow>=0 and currCol<=n-1:
                if (currRow+1)*(currCol+1)>num:
                    currRow -= 1
                else:
                    currCnt += (currRow+1)
                    currCol += 1
            return currCnt>=k
            
        left, right = 1, m*n
        while left<right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        