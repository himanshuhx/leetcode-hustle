'''
to find the kth smallest element in a row and column wise sorted matrix

one approach is to use max heap
another is to take advantage of sorted matrix and apply binary search
we know as matrix is sorted so minimum and max ele will be at (0,0) and (n-1,n-1) index
apply binary search over the range... 
we have to check whether curr mid is feaible or not if yes we need to shrink right part 
else shrink left part
ques is how feasible or (counting the no less than mid) is O(n) operation?

we are running loop from first row , last col if we encounter an ele > mid we just move up row--
else if we meet an ele <= mid we know all ele above this row will be smaller than mid
currCount += currRow + 1 and col++ 
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def feasible(target):
            currCount = 0
            n = m = len(matrix)
            currCol , currRow = 0, n-1
            while currRow>=0 and currCol<=n-1:
                if matrix[currRow][currCol]>target:
                    currRow -= 1
                else:
                    currCount += currRow+1
                    currCol += 1
            return currCount>=k
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left<right:
            mid = left + (right - left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        