class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0]*n
        lastLogTimeStamp = -1
        stack = []
        
        for log in logs:
            logId, event, timeStamp = log.split(":")
            
            logId, timeStamp  = int(logId), int(timeStamp)
            
            if event == "end":
                timeStamp += 1
                
            if stack:
                currExecuting = stack[-1]
                ans[currExecuting] += timeStamp-lastLogTimeStamp
                
            if event=="start":
                stack.append(logId)
            else:
                stack.pop()
                
            lastLogTimeStamp = timeStamp
            
        return ans
        
        
        