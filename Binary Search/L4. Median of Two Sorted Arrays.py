class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        left, right = 0, n1 #where to place cut
        while left <= right:
            cut1 = left + (right-left)//2
            cut2 = (n1+n2+1)//2 - cut1
            
            if cut1:
                left1 = nums1[cut1-1]
            else:
                left1 = -float("inf")
                
            if cut2:
                left2 = nums2[cut2-1]
            else:
                left2 = -float("inf")
                
            if cut1!=n1:
                right1 = nums1[cut1]
            else:
                right1 = float("inf")
                
            if cut2!=n2:
                right2 = nums2[cut2]
            else:
                right2 = float("inf")               
            
            if left1<=right2 and left2<=right1:
                if (n1+n2)%2==0:
                    return (max(left1,left2)+min(right1,right2))/2
                else:
                    return max(left1,left2)
            elif left1>right2:
                right = cut1-1
            else:
                left = cut1+1
        return 0.0     