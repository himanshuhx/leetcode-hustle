class Solution:

    # Dynamic programming approach
    def checkValidString(self, s: str) -> bool:
        def check(st):
            stack = []
            for i in range(len(st)):                
                if stack and st[i]==')' and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(st[i])
            return len(stack)==0
        
        def solve(t,i):
            if i==len(t):
                return check(t)
            key = (t,i)
            if key in memo:
                return memo[key]
            if t[i]!='*':
                memo[key] = solve(t,i+1)
            else:
                t1 = t[:i]+'('+t[i+1:]
                t2 = t[:i]+')'+t[i+1:]
                t3 = t[:i] + t[i+1:]
                memo[key] = solve(t1,i+1) or solve(t2,i+1) or solve(t3,i+1)
            return memo[key]
        
        memo = {}
        return solve(s,0)
    
    # Two Stacks Approach O(N), O(N)
    def checkValidString(self, s: str) -> bool:
        openn, star = [], []
        for i in range(len(s)):
            if s[i]=='(':
                openn.append(i)
            elif s[i]=='*':
                star.append(i)
            else:
                if openn:
                    openn.pop()
                elif star:
                    star.pop()
                else:
                    return False
                
        if openn:
            while openn and star and openn[-1]<star[-1]:
                openn.pop()
                star.pop()
            if openn:
                return False
        return True
                