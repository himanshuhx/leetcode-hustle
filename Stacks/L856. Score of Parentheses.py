class Solution:

    # O(N) O(N)
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for x in s:
            if x=='(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2*v,1)
        return stack.pop()

    # O(N) O(1)
    def scoreOfParentheses(self, s: str) -> int:
        ans, depth = 0, 0
        for i in range(len(s)):
            if s[i]=='(':
                depth+=1
            else:
                depth-=1
                if s[i-1]=='(':
                    ans += (2**depth)
        return ans