class Solution:
    def maxDistance(self, position : List[int], m: int) -> int:
        def feasible(M):
            total, currPlaced = 1, position[0]
            for i in range(len(position)):
                if position[i]-currPlaced>=M:
                               total+=1
                               currPlaced = position[i]
            return total<m
                
        position.sort()
        left, right,  = 1, position[-1]
        while left<right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left-1