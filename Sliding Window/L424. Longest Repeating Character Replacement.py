class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count, i, j = 0, 0, 0
        count, maxi = {}, -float("inf")
        while j<len(s):
            count[s[j]] = count.get(s[j],0)+1
            max_count = max(max_count,count[s[j]])
            if j-i+1-max_count>k:
                count[s[i]]-=1
                i+=1
            maxi = max(maxi,j-i+1)
            j+=1
        return maxi