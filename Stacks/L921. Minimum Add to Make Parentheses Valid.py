class Solution:

    # O(N) O(N)
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for x in s:
            if stack and x==')' and stack[-1]=='(':
                stack.pop()
            else:
               stack.append(x)
        return len(stack)
    
    # O(N) O(1)
    def minAddToMakeValid(self, s: str) -> int:
        ans, bal = 0, 0
        for x in s:
            if x=='(':
                bal += 1
            else:
                bal -= 1
            if bal==-1:
                bal += 1
                ans += 1
        return ans + bal