class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')':'(','}':'{',']':'['}
        for x in s:
            if x in dict.values():
                stack.append(x)
            elif x in dict.keys():
                if not stack or dict[x]!=stack.pop():
                    return False
        return stack==[]
        