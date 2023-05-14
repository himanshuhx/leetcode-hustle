class Solution:

    # O(N) for getting count of b before any index + O(N) for a count + O(N) for mini
    # O(N)+O(N) -> space
    def minimumDeletions(self, s: str) -> int: 
        mini = 10000000
        n = len(s)
        noOfbBefore = [0]*n
        noOfaAfter = [0]*n
        
        for i in range(1,n):
            if s[i-1]=='b':
                noOfbBefore[i] = noOfbBefore[i-1] + 1
            else:
                noOfbBefore[i] = noOfbBefore[i-1]
            
        for i in range(n-2,-1,-1):
            if s[i+1]=='a':
                noOfaAfter[i] = noOfaAfter[i+1] + 1
            else:
                noOfaAfter[i] = noOfaAfter[i+1]
        
        
        for i in range(n):
            mini = min(mini,noOfbBefore[i]+noOfaAfter[i])
            
        return mini
    
    # O(N) O(N)
    def minimumDeletions(self, s: str) -> int:
        stack = []
        count=0
        for x in s:
            if stack and stack[-1]=='b' and x=='a':
                stack.pop()
                count+=1
            else:
                stack.append(x)
            
        return count