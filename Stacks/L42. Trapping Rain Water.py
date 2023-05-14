'''
vvimp quest for interview we have to find the total amount of rainwater trapped within blocks

Intuition --> find nearest LEFTMOST and RIGHTMOST tall buiding.
              The amount of water trapped = min(LEFTMOST,RIGHTMOST)- nums[i] (currHeight)
 
This is the only way to find we can optimise our soln by optimizing the way to find
left and right values.

Approach 1 ---> Brute Force O(N^2) O(1)
for every index find LEFTMOST next Taller for(i-1 --> 0)
for every index find RIGHTMOST next Taller for(i+1 --> n-1)
res += min(LEFTMOST,RIGHTMOST)- nums[i] (currHeight)

Approach 2 ---> Maintain Prefix and Suffix array for left and right heights
O(N)+O(N)+O(N), O(2*N)
'''
class Solution:
    def trap(self, arr: List[int]) -> int:
        if not arr:
            return 0
        n = len(arr)
        pre, suff = [0]*n, [0]*n
        maxL, maxR = arr[0], arr[-1]
        for i in range(n):
            maxL = max(maxL, arr[i])
            pre[i] = maxL
        for i in range(n-1,-1,-1):
            maxR = max(maxR, arr[i])
            suff[i] = maxR
        res = 0
        for i in range(n):
            res += min(pre[i], suff[i]) - arr[i]
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        i, j, maxLeft, maxRight = 0, len(height)-1, 0, 0
        water = 0
        while i<j:
            
            # i<j which means there will be a slope and water will be accumulating like
            #          /j
            #         /
            #        /
            #      i/
            # so work on ith pointer
            if height[i]<=height[j]:
                maxLeft = max(maxLeft,height[i])
                water += maxLeft-height[i]
                i+=1
                
            # i>j which means there will be a slope and water will be accumulating like
            #       i\
            #         \
            #          \
            #           \j
            # so work on jth pointer
            else:
                maxRight = max(maxRight,height[j])
                water += maxRight-height[j]
                j-=1
                
                
        return water

'''
Difference/Similarities between Trapping Rain Water and Largest rectangle in Histogram.

Trapping Rain Water
-------------------

        Right----
                |
                |----> take minimum - arr[i] 
                |
        Left-----

Largest rectangle In Histogram
------------------------------

        Right----
                |
                |----> minus * arr[i] 
                |
        Left-----

'''