# T.C -> O(N*(4^N))

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(start, k, curr):
            if k==0:
                perms.append(''.join(curr[:]))
                return
            
            for next_char in combo[digits[start]]:
                curr.append(next_char)
                dfs(start+1, k-1, curr)
                curr.pop()
        
        
        if not digits:
            return []
        
        combo = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", 
                 "7":"pqrs", "8":"tuv", "9":"wxyz"}
        perms = []
        dfs(0, len(digits), [])
        return perms