from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        
        low, high = 0, (n * m)-1
        
        while low<=high:
            
            mid = (low+high)//2
            
            if matrix[mid//m][mid%m] == target:
                return True
            if matrix[mid//m][mid%m]<target:
                low = mid+1            
            else:
                high = mid-1
                
        return False
        