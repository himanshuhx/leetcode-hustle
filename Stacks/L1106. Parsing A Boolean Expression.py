class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for i in range(len(expression)):
            
            if expression[i]==')':
                
                seen = set()
                while stack and stack[-1]!='(':
                    seen.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                
                if operator=='&':
                    if 'f'in seen:
                        stack.append('f')
                    else:
                        stack.append('t')
                elif operator=='|':
                    if 't'in seen:
                        stack.append('t')
                    else:
                        stack.append('f')
                else:
                    if 't' in seen:
                        stack.append('f')
                    else:
                        stack.append('t')      
                        
            elif expression[i]!=',':
                stack.append(expression[i])
                
        return stack[-1]=='t'
                    
                
                    