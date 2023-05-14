class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def solve(i,m,n):
            if m==0 and n==0:
                return 0
            if i<0:
                return 0
            key = (i,m,n)
            if key in memo:
                return memo[key]
            ones, zeroes = 0, 0
            for bit in strs[i]:
                if bit == '1':
                    ones+=1
                else:
                    zeroes+=1
            if m>=zeroes and n>=ones:
                memo[key] = max(solve(i-1,m-zeroes,n-ones)+1, solve(i-1,m,n))
            else:
                memo[key] = solve(i-1,m,n)
            return memo[key]
        
        memo = {}
        res = solve(len(strs)-1,m,n)
        return 0 if res == -float("inf") else res