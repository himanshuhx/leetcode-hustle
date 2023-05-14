class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxi = 0
        for x in s:
            if stack and x=='(' and stack[-1]==')':
                stack.pop()
            elif x=='(':
                stack.append(x)
            elif x==')' and stack:
                stack.pop()
            maxi = max(maxi,len(stack))
        #print(stack)
        return maxi