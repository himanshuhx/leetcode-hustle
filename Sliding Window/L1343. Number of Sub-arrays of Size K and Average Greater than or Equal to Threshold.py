class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i, j = 0, 0
        count, currWindowSum, currWindowAvg = 0, 0, 0
        for j in range(len(arr)):
            currWindowSum += arr[j]
            if j-i+1 == k:
                currWindowAvg = currWindowSum//k
                if currWindowAvg>=threshold:
                    count+=1
                currWindowSum -= arr[i]
                i+=1
                j+=1
        return count
        