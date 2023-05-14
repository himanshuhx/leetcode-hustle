class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for x in s:
            stack.append(x)
            if len(stack)>2:
                curr = stack[-3]+stack[-2]+stack[-1]
                if curr=="abc":
                    for i in range(3):
                        stack.pop()
            
        return len(stack)==0