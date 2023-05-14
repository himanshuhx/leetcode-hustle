def knapSackRecursive(wt,val,knapSackWeight,n):
    if n==0 or knapSackWeight==0:
        return 0
    if wt[n-1]<=knapSackWeight:
        return max(val[n-1]+knapSackRecursive(wt,val,knapSackWeight-wt[n-1],n-1),knapSackRecursive(wt,val,knapSackWeight,n-1))
    else:
        return knapSackRecursive(wt,val,knapSackWeight,n-1)

def knapSackMemoized(wt,val,knapSackWeight,n):    
    global memo
    if n==0 or knapSackWeight==0:
        return 0
    if memo[n-1][knapSackWeight-1]!=-1:
        return memo[n-1][knapSackWeight-1]
    else:
        if wt[n-1]<=knapSackWeight:
            memo[n-1][knapSackWeight-1]=max(val[n-1]+knapSackRecursive(wt,val,knapSackWeight-wt[n-1],n-1),knapSackRecursive(wt,val,knapSackWeight,n-1))
            return memo[n-1][knapSackWeight-1]
        else:
            memo[n-1][knapSackWeight-1] = knapSackRecursive(wt,val,knapSackWeight,n-1)
            return memo[n-1][knapSackWeight-1]

wt = list(map(int,input().split()))
val = list(map(int,input().split()))
knapSackWeight = int(input())
n = len(wt)
memo = [[-1 for j in range(knapSackWeight + 1)] for i in range(n + 1)]
#print(knapSackRecursive(wt,val,knapSackWeight,n))
print(knapSackMemoized(wt,val,knapSackWeight,n))