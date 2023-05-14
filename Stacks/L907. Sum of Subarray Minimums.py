class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left, right, stack =[0]*len(arr), [0]*len(arr), []

        for i in range(len(arr)):
            curr_ele = arr[i]
            count=1
            while len(stack)>0 and stack[-1][0]>curr_ele:
                count += stack[-1][1]
                stack.pop()
            stack.append([curr_ele,count])
            left[i]=count
        stack.clear()
        
        for i in range(len(arr)-1,-1,-1):
            curr_ele = arr[i]
            count=1
            while len(stack)>0 and stack[-1][0]>=curr_ele:
                count += stack[-1][1]
                stack.pop()
            stack.append([curr_ele,count])
            right[i]=count
            
        ans=0
        mod=10**9+7
        for i in range(len(arr)):
            ans= ans + (left[i]*right[i]*arr[i])%mod
        return ans%mod
        