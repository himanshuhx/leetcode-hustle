class Solution:

    # O(N^2),  O(N)
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for x in s:
            if x!=')':
                stack.append(x)
            else:
                ans = ""
                while stack and stack[-1]!='(':
                    ans += stack.pop()
                stack.pop()   
                if ans:
                    for i in range(len(ans)):
                        stack.append(ans[i])
        return ''.join(stack)