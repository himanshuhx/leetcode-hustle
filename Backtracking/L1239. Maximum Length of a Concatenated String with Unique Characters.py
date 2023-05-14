'''
One point to be noted in combination type problems template looks like

def dfs([start], curr):
    // base case
    if start>=n:
        # do something
        return

    // choices

    for j in range(start, n):

        curr.append(...)
        [ dfs(j+1,curr) ]---> dfs starts from j+1
        curr.pop()

'''


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(i, curr):
            if i>=len(arr):
                return                                  
            for j in range(i, len(arr)):
                for c in arr[j]:
                    curr.append(c)
                if len(curr)==len(set(curr)):
                    self.ans = max(self.ans, len(curr))
                    dfs(j+1, curr)
                for k in range(len(arr[j])):
                    curr.pop()
        
        self.ans = 0
        dfs(0, [])
        return self.ans