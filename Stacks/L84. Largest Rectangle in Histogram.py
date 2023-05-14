'''
Approach 1 (Naive approach)

For every index i we find left smaller and right smaller. O(N)
--> width of histogram 
    left side --> index after smaller in left  --> idxLeft = idx + 1
    right side --> index before smaller in right --> idxRight = idx - 1
    width = (idxRight - idxLeft) * arr[i]

Computing for every index will make this approach be O(N^2) and O(1) space
'''
# next smaller from left and right and storing it in array
# O(N)+O(N)+O(N), O(2*N)
# we can reduce one pass by calculating and updating our ans during filling rightIdx.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        leftIdx, rightIdx = [], []
        stack, n = [], len(heights)
        
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                leftIdx.append(stack[-1]+1)
            else:
                leftIdx.append(0)
            stack.append(i)
        stack.clear()
        
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                rightIdx.append(stack[-1]-1)
            else:
                rightIdx.append(n-1)
            stack.append(i)        
        rightIdx = rightIdx[::-1]
        
        ans = 0
        for i in range(n):
            ans = max(ans, (rightIdx[i]-leftIdx[i]+1)*heights[i])
            
        return ans