class Solution:

    #  ~O(N), O(N)
    def decodeString(self, s: str) -> str:
        stack = []
        
        for x in s:
            if x!="]":
                stack.append(x)
            else:
                curr = ""
                while stack[-1]!="[":
                    curr = stack.pop() + curr
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                    
                stack.append(curr*int(num))
                
        return "".join(stack)
        