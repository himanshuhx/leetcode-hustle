# https://www.youtube.com/watch?v=Fha1CSxwvGg
# Amazon

class Solution:
    def grayCode(self, n: int) -> List[int]:
        def solve(n):
            if n==1:
                return ["0","1"]
            temp = solve(n-1)
            res = []
            for i in range(len(temp)):
                res.append("0" + temp[i])
            for i in range(len(temp)-1,-1,-1):
                res.append("1" + temp[i])
            return res
        
        ans = []
        ans = solve(n)
        for i in range(len(ans)):
            ans[i] = int(ans[i], 2)
        return ans

#  https://leetcode.com/problems/gray-code/discuss/29893/One-liner-Python-solution-(with-demo-in-comments)
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for x in reversed(res):
                res.append(x+(2**i))
        return res