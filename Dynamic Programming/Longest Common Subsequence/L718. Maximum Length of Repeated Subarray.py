class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:  
        m, n = len(nums1), len(nums2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        ans = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j]=0
                ans = max(ans,dp[i][j])
        return ans
                         
    def solve(n,m,count):
            if n<0 or m<0:
                return count
            
            key =(n,m,count)
            if key in memo:
                return memo[key]
            
            if nums1[n]==nums2[m]:
                count = solve(n-1,m-1,count+1)
            memo[key] = max(count,solve(n-1,m,0),solve(n,m-1,0))
            
            return memo[key]
        
        memo = {}
        return solve(len(nums1)-1,len(nums2)-1,0)
