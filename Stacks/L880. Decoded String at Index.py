class Solution:

    # Naive memory limit exceeded
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        for x in s:
            if x.isdigit():
                temp = stack
                for i in range(int(x)-1):
                    stack = stack+temp
            else:
                stack.append(x)
        return stack[k-1]
    
    # O(N) O(1)
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for x in s:
            if x.isdigit():
                size *= int(x)
            else:
                size += 1
                
        for x in reversed(s):
            k %= size
            if k==0 and x.isalpha():
                return x
            if x.isdigit():
                size/=int(x)
            else:
                size-=1
                
        return ""
            