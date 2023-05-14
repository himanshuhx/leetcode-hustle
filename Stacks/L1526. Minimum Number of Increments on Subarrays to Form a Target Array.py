class Solution:

    # two stack approach vvvimp (largest histogram type)
    def minNumberOperations(self, target: List[int]) -> int:
        def getNextSmallerToLeft():
            nextSmallerToLeft, stack = [], []
            for i in range(len(target)):
                while stack and stack[-1]>target[i]:
                    stack.pop()
                if not stack:
                    nextSmallerToLeft.append(0)
                else:
                    nextSmallerToLeft.append(stack[-1])
                stack.append(target[i])
            return nextSmallerToLeft
        
        def getNextSmallerToRight():
            nextSmallerToRight, stack = [], []
            for i in range(len(target)-1,-1,-1):
                while stack and stack[-1]>=target[i]:
                    stack.pop()
                if not stack:
                    nextSmallerToRight.append(0)
                else:
                    nextSmallerToRight.append(stack[-1])
                stack.append(target[i])
            return nextSmallerToRight
            
            
            
        nextSmallerToRight, nextSmallerToLeft = getNextSmallerToRight(), getNextSmallerToLeft()
        ans = 0
        nextSmallerToRight = nextSmallerToRight[::-1]
        for i in range(len(target)):
            ans += target[i]-max(nextSmallerToRight[i], nextSmallerToLeft[i])
        return ans

    # O(N) O(1)  
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        peek = 0
        for i in range(len(target)):
            if target[i]>peek:
                ans += (target[i]-peek)
            peek = target[i]               
        return ans