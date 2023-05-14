class Solution:
    # vvvimp amazon's fav
    # O(N), O(N)
    # ths can also be done in O(1) by maintaing a variable last_number instead of stack
    def calculate(self, s: str) -> int:
        stack, curr_num, operator = [], 0, "+"
        all_operators = set(["+","-","*","/"])
        for i,x in enumerate(s):
            if x.isdigit():
                curr_num = curr_num*10 + int(x)
            if x in all_operators or i==len(s)-1:
                
                if operator=="+":
                    stack.append(curr_num)
                    
                elif operator=="-":
                    stack.append(-curr_num)
                    
                elif operator=="*":
                    stack[-1]*=curr_num
                    
                elif operator=="/":
                    stack[-1] = int(stack[-1]/curr_num)
                    
                curr_num = 0
                operator = x
                
        return sum(stack)
                