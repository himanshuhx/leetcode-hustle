class Solution:

    # O(N) O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        # stack will have indices at last whose balanced parantheses wee not found 
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if stack and s[stack[-1]]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        j = 0
        ans = ''

        # iterate over main string and skip those indices which are in stack
        for i in range(len(s)):
            if j<len(stack) and i==stack[j]:
                j+=1
            else:
                ans += s[i]
        return ans
            
                