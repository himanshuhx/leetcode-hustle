# https://www.youtube.com/watch?v=HAA8mgxlov8
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            match = i<len(s) and (s[i]==p[j] or p[j]=='.')
            if j+1<len(p) and p[j+1]=='*':
                return solve(i,j+2) or (match and solve(i+1,j)) 
            if match:
                return solve(i+1,j+1)
            return False
        return solve(0,0)