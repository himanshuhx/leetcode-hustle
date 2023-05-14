class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)>(len(s1)+len(s2)):
            return False
        def solve(i,j,k):
            if i>=len(s1) and j>=len(s2) and k>=len(s3):
                return True
            if k>=len(s3):
                 return False

            key = (i,j)
            if key in memo:
                return memo[key]

            if i<len(s1) and s1[i]==s3[k] and j<len(s2) and s2[j]==s3[k]:
                memo[key] = solve(i+1,j,k+1) or solve(i,j+1,k+1)
            elif i<len(s1) and s1[i]==s3[k]:
                memo[key] = solve(i+1,j,k+1)           
            elif j<len(s2) and s2[j]==s3[k]:
                memo[key] = solve(i,j+1,k+1)
            else:
                memo[key] = False
                
            return memo[key]
            
        memo = {}
        return solve(0,0,0)
        