### vvimp although tagged in easy!!!

class Solution:

    # Time complexity O(S+T)   Space complexity- O(S+T)
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for x in s:
                if x=='#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(x)
            return ''.join(stack)

        return build(s)==build(t)


    # Time complexity O(S+T)   Space complexity- O(1)   
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        while i>=0 or j>=0:
            
            count = 0
            while i>=0:
                if s[i]=='#':
                    count+=1
                    i-=1
                elif s[i]!='#' and count>0:
                    count-=1
                    i-=1
                else:
                    break
                    
            count = 0            
            while j>=0:
                if t[j]=='#':
                    count+=1
                    j-=1
                elif t[j]!='#' and count>0:
                    count-=1
                    j-=1
                else:
                    break
                    
            if (i<0 and j>=0) or (i>=0 and j<0):
                return False
            
            if i>=0 and j>=0 and s[i]!=t[j]:
                return False
            
            i-=1
            j-=1
        return True