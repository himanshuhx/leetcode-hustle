# Time Complexity for any backtracking/ recursive soln can be analysed as 
# (choices made/ branches of tree) ^ n(height of tree)

# here since at most we will be making three choices as no should be <256
# height of tree can be upto height 12 i.e valid s length
# thus time complexity is 3^12 in worst case.


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def solve(i, dotCnt, curr):
            if i>=len(s) and dotCnt==4:
                ans.append(curr[:-1])
                return
            
            for j in range(i, min(i+3, n)):
                if int(s[i:j+1])<256 and (i==j or s[i]!="0"):
                    solve(j+1, dotCnt+1, curr + s[i:j+1] + ".")

        
        n = len(s)
        if n<4 or n>12: return []
        ans = []
        solve(0, 0, "")
        return ans