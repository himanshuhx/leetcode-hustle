'''
we have a bloomday array which shows the day at which flower will bloom
we have to make m bouquets where each bouque will have k flowers (flowers should be adjacent)

find min day to make bouquets if not possible return -1
'''

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(threshold):
            bouqueCount, flowerCount = 0, 0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=threshold:
                    flowerCount += 1
                else:
                    flowerCount = 0  # if flowers are not continuous
                    
                if flowerCount == k:
                    bouqueCount += 1
                    flowerCount = 0
            return bouqueCount>=m
        
        if len(bloomDay) < m*k:  # flowers required are more than flower present in array
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        while left<right:
            mid = left + (right - left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left