class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        s, e = 0, n-1
        while s+1<n and arr[s]<=arr[s+1]:
            s+=1
        if s==n-1:
            return 0
        while e-1>=0 and arr[e-1]<=arr[e]:
            e-=1
        if e==0:
            return n-1
        result = min(n-1-s,e)
        
        i, j = 0, e
        while i<=s and j<n:
            if arr[i]<=arr[j]:
                result = min(result,j-i-1)
                i+=1
            else:
                j+=1
        return result