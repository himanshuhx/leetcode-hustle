'''
we need to find the min weight carrying capacity of ship so that all the weight is transported 
in D days.

left and right is intialized to max(weights) and sum(weights) because our ans will lie between
them...we will greedily start trying to search for our ans and minimizing the search space 
for every mid (our current expected capacity) we will call feasible() to check whether it is 
possible to carry that weight=mid within d days if yes than we will reduce our search space
because we can get more less value on left 

feasible simply traverses the array and keeps adding weight to currWeight until its exceed capacity
if capacity is exceeded it means we cannot transport ths weight today and it will have to be transported
tomorrow so now we need one extra days so we increase the days and assign currWeight to weight[i]
curr index weight this updation is needed because we have transported previous weights yesterday
also we keep a check on days if it exceed D we return False.
if whole weight is transported and our days doesnt exceeded our max D we return True

'''

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity,D):
            days = 1
            currWeight = 0
            for weight in weights:
                currWeight += weight
                if currWeight>capacity:
                    days+=1
                    currWeight = weight
                if days>D:
                    return False
            return True
        
        left, right = max(weights), sum(weights)
        while left<right:
            mid = left + (right-left)//2
            if feasible(mid,days):
                right = mid
            else:
                left = mid + 1
        return left