class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        lastSeenIndex = {}
        seen = [False]*26
        
        for i in range(len(s)):
            lastSeenIndex[s[i]] = i
            
        for i in range(len(s)):
            if not seen[ord(s[i])-97]:
                while stack and ord(stack[-1]) > ord(s[i]) and i < lastSeenIndex[stack[-1]]:
                    seen[ord(stack.pop())-97]=False
                stack.append(s[i])
                seen[ord(s[i])-97]=True
                
        return ''.join(stack)