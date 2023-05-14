def solve(idx,memo):
    if idx<0:
        return 0
    if memo[idx]!=-1:
        return memo[idx]
    if idx==0 or idx==1:
        return cost[idx]
    memo[idx] = cost[idx]+min(solve(idx-1,memo),solve(idx-2,memo))
    return memo[idx]

def solve(idx):
    if idx<0:
        return 0
    if idx==0 or idx==1:
        return cost[idx]
    return cost[idx]+min(solve(idx-1),solve(idx-2))

cost = list(map(int,input().split()))
n = len(cost)
memo = [-1]*n
print(min(solve(n-1,memo),solve(n-2,memo)))
print(min((solve(n-1),solve(n-2))))
