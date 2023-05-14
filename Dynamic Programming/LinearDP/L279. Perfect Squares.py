def recursive(n):
    if n==0:
        return 0
    if n<0:
        return float("inf")
    mini = n
    i = 1
    while i*i<=n:
        mini = min(mini, recursive(n-(i*i)))
        i+=1
    return mini+1


def memoized(n):
    if n==0:
        return 0
    if n<0:
        return float("inf")
    if memo[n]!=-1:
        return memo[n]
    mini = n
    i = 1
    while i*i<=n:
        mini = min(mini, memoized(n-(i*i)))
        i+=1
    memo[n] = mini+1
    return memo[n]

n = int(input())   
memo = [-1]*(n+1)
print(recursive(n))
print(memoized(n))