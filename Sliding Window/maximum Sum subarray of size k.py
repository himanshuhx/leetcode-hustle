'''
given an array find the max of sum of all subarrays of size k.

fixed size window problem.

'''
def slidingWindow(nums,k): 
    i, j = 0, 0
    maxi = -float("inf")
    currWindowSum = 0
    while j<len(nums):

        if j-i+1<k:   # curr window size is less than k (preprocessing part)
            currWindowSum += nums[j]
            j+=1

        elif j-i+1 == k:    # add curr ele remove prev ele check for max
            currWindowSum += nums[j]
            maxi = max(maxi,currWindowSum)
            currWindowSum -= nums[i]

            i+=1
            j+=1

    return maxi

print(slidingWindow([2,1,-3,4,7,6],3))