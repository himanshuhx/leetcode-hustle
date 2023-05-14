'''
all calculator series question namey I II and III can be solved using this template

in I --> + - ( ) are present
in II --> + - * / are present
in III --> + - * / ( ) are present

we can use II as a method and solve others 

'''

# O(N^2) O(N)
# O(N) --> extra because we are slicing string every time and a case like (1+(1+(1+...)))
# will make O(N)*O(N)
# to get read of this we can pass index as reference
class Solution:
    def calculate(self, s: str) -> int:
        
        def calc(operator, curr_num):
            if operator == '+': stack.append(curr_num)
            elif operator == '-': stack.append(-curr_num)
            # uncomment below for Calculator III
            #elif operator=='*': stack.append(int(stack.pop())*curr-num) 
            #else: stack.append(int(stack.pop())//curr_num)
                
        curr_num, stack, operator = 0, [], "+"
        i = 0
        while i < len(s):
            
            if s[i].isdigit():
                curr_num = curr_num*10 + int(s[i])
            elif s[i] in "+-*/":
                calc(operator, curr_num)
                curr_num, operator = 0, s[i]
            elif s[i] == '(':
                curr_num, j = self.calculate(s[i+1:])
                i += j
            elif s[i] == ')':
                calc(operator, curr_num)
                return sum(stack), i+1
            
            i+=1
            
        calc(operator, curr_num)
        return sum(stack)