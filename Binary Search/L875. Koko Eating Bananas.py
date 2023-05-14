'''
similar to ship capacity problem

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile/speed)
            return time<=h
        
        tBananas = sum(piles)
        left, right = 1, max(piles)
        while left<right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left