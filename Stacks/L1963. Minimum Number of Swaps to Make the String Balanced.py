class Solution:

    # O(N), O(N)
    def minSwaps(self, s: str) -> int:
        stack = []
        for x in s:
            if x=='[':
                stack.append(x)
            elif x==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(x)
        l = len(stack)//2   # unmatched brackets of each type
        return math.ceil(l/2) if stack else 0

    
    # O(N), O(1)
    def minSwaps(self, s: str) -> int:
        notMatched = 0
        for x in s:
            if x=='[':
                notMatched+=1
            elif x==']':
                if notMatched>0:
                    notMatched-=1
        return math.ceil(notMatched/2) if notMatched else 0