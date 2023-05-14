class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def solve(s1,s2):
            key = (s1,s2)
            if key in memo:
                return memo[key]
            if s1==s2:
                return True
            if len(s1)<=1 or len(s2)<=1:
                return False
            
            n = len(s1)
            memo[key]=False
            for k in range(1,n):
                swap = solve(s1[:k],s2[n-k:]) and solve(s1[k:],s2[:n-k])
                noSwap = solve(s1[:k],s2[:k]) and solve(s1[k:],s2[k:])
                if swap or noSwap:
                    memo[key] = True
                    break
            return memo[key]
            
        
        if not s1 and not s2:
            return True
        if len(s1)!=len(s2):
            return False
        memo = {}
        return solve(s1,s2)
    