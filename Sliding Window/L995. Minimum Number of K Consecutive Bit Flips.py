class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hasEverFlipped = [0]*n
        countOfValidFlipFromStartOfWindowToCurrIdx = 0
        ans = 0
        for i in range(n):
            if i>=k:
                countOfValidFlipFromStartOfWindowToCurrIdx -= hasEverFlipped[i-k]
            if countOfValidFlipFromStartOfWindowToCurrIdx%2 == nums[i]:
                if i+k>n:
                    return -1
                countOfValidFlipFromStartOfWindowToCurrIdx += 1
                hasEverFlipped[i]=1
                ans+=1
        return ans
        
                    