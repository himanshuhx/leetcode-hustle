from collections import deque
def slidingWindow(nums,k):
    neg, ans = deque(), []
    i, j = 0, 0
    while j<len(nums):
        
        if nums[j]<0:
                neg.append(nums[j])
                
        if j-i+1<k:
            j+=1
            
        elif j-i+1==k:
            if not neg:
                ans.append(0)
            else:
                ans.append(neg[0])
            
            if neg and neg[0]==nums[i]:
                neg.popleft()
            
            j+=1
            i+=1
    return ans

print(slidingWindow([2,-1,-3,4,-7,6],3))