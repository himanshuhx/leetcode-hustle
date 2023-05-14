### vvimp 
# O(N) O(1)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        i=0
        
        for i in range(n):   
            stack.append(asteroids[i])
            while len(stack)>1 and stack[-1]<0 and stack[-2]>0:
                if abs(stack[-2])==abs(stack[-1]): # both will destroy
                    stack.pop()
                    stack.pop()
                    break
                elif abs(stack[-1])>stack[-2]:
                    stack.pop(-2)
                else:
                    stack.pop()   
                            
        return stack
                
                
 