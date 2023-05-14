#leetcode 842
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def dfs(i):
            if i>=len(num):
                return len(ans)>2           
            n = 0
            for j in range(i, len(num)):
                n = n*10 + int(num[j]) 
                if n>2**31: # if number exceeds the range mentioned
                    return False
                if len(ans)<2 or (ans[-1]+ans[-2]==n):
                    ans.append(n)
                    if dfs(j+1):
                        return True
                    ans.pop()
                if i==j and num[j]=='0': # if trailing 0 is present
                    return False
        

        if len(num)<=2: return []
        ans = []
        if dfs(0): return ans
        return []
#--------------------------------------------------------------------------------------------------
#leetcode 306
class Solution:
    def isAdditiveNumber(self, num: str) -> List[int]:
        def dfs(i, ans):
            if i>=len(num):
                return len(ans)>2           
            n = 0
            for j in range(i, len(num)):
                n = n*10 + int(num[j]) 
                if len(ans)<2 or (ans[-1]+ans[-2]==n):
                    ans.append(n)
                    if dfs(j+1, ans):
                        return True
                    ans.pop()
                if i==j and num[j]=='0': 
                    return False
        
        return dfs(0, []) 
#-----------------------------------------------------------------------------------------------
#leetcode 1849
class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(i, ans):
            if i>=len(s):
                return len(ans)>1           
            n = 0
            for j in range(i, len(s)):
                n = n*10 + int(s[j]) 
                if len(ans)<1 or (ans[-1]-1==n):
                    ans.append(n)
                    if dfs(j+1, ans):
                        return True
                    ans.pop()
        
        return dfs(0, [])