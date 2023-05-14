# Brute force (TLE)
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        maxi = -float("inf")
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                    x = abs(points[i][0]-points[j][0])
                    if x<=k:
                        y = points[i][1]+points[j][1]
                        maxi = max(maxi,x+y)
        return maxi