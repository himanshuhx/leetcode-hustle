class Solution:

    # stack with greedy approach 
    # O(N)+O(N) , O(N)
    def maximumGain(self, s: str, x: int, y: int) -> int:
        money = 0
        
        def calc(a,price,remove):
            nonlocal money
            stack = []
            for i in range(len(a)):
                stack.append(a[i])
                while len(stack)>1 and stack[-2]==remove[0] and stack[-1]==remove[1]:
                    stack.pop()
                    stack.pop()
                    money += price
            return ''.join(stack)
        
        if x>y:
            s = calc(s,x,'ab')
            t = calc(s,y,'ba')
        else:
            s = calc(s,y,'ba')
            t = calc(s,x,'ab')
            
        return money