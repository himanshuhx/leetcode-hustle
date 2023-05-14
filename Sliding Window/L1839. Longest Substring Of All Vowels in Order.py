class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        maxi, j = 0, 1
        count = unique = 1
        while j<len(word):
            if word[j-1]<=word[j]:
                count+=1
                if word[j-1]<word[j]:
                    unique+=1
            else:
                count = unique = 1
            if unique==5:
                maxi = max(maxi,count)
            j+=1
        return maxi