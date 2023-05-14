class Solution:


    # O(N) O(1)
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxi, count = -1, 0
        for i in range(len(arr)):
            maxi = max(maxi,arr[i])
            if i==maxi:
                count+=1
        return count