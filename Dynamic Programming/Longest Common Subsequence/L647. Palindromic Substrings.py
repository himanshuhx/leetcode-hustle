# vvvimp 0n^2 expand from center
# https://www.youtube.com/watch?v=4RACzI5-du8

class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(l,r):
            res=0
            while l>=0 and r<=n-1 and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        
        res = 0
        n = len(s)
        for i in range(n):
            res += count(i,i)  # count odd length
            res += count(i,i+1) #count even length
        return res