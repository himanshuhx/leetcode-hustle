## largest area in histogram similar

# O(row*col)

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def getAreaOfHistogram(nums):
            leftIdx, rightIdx = [], []
            stack, n = [], len(nums)
            
            for i in range(n):
                while stack and nums[stack[-1]]>=nums[i]:
                    stack.pop()
                if stack:
                    leftIdx.append(stack[-1]+1)
                else:
                    leftIdx.append(0)
                stack.append(i)
            stack.clear() 
            
            for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]]>=nums[i]:
                    stack.pop()
                if stack:
                    rightIdx.append(stack[-1]-1)
                else:
                    rightIdx.append(n-1)
                stack.append(i)
            rightIdx = rightIdx[::-1]
                    
            maxi = 0
            for i in range(n):
                maxi = max(maxi, (rightIdx[i]-leftIdx[i]+1)*nums[i])
                
            return maxi
        
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        histogram = [0]*cols
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=="0":
                    histogram[j]=0
                else:
                    histogram[j]+=1
            maxArea = max(maxArea, getAreaOfHistogram(histogram))
        return maxArea
                
            