class Solution:

    # O(N*(2*k)) ~ O(N*K), O(N) 
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for x in s:

            stack.append(x)
            
            if stack and len(stack)>=k:
                curr = stack[-1]
                flag = True
                for i in range(1,k+1):
                    if curr!=stack[-i]:
                        flag = False
                if flag:
                    for i in range(k):
                        stack.pop()
            
        return ''.join(stack)

    # O(N) O(N) by maintaing list -> [element, count]
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for x in s:         
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
            else:
                stack.append([x,1])
                
            if stack and stack[-1][1] == k:
                stack.pop()
            
        ans = ""
        for x in stack:
            ans += str(x[0])*int(x[1])
        return ans