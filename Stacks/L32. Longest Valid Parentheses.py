class Solution:

    # O(N), O(N) using stack
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxi = 0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxi = max(maxi,i-stack[-1])
        return maxi

    # O(N), O(1)
    def longestValidParentheses(self, s: str) -> int:
        maxi = 0
        openn, close = 0, 0
        for x in s:
            if x=='(':
                openn+=1
            else:
                close+=1
            if openn==close:
                maxi = max(maxi,openn*2)
            elif close>openn:
                openn=close=0
        
        openn=close=0
        for x in s[::-1]:
            if x=='(':
                openn+=1
            else:
                close+=1
            if openn==close:
                maxi = max(maxi,openn*2)
            elif openn>close:
                openn=close=0                     
        
        return maxi