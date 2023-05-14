class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i, j = 0, 0
        currCost, maxi = 0, 0
        while j<len(s):
            currCost += abs(ord(s[j])-ord(t[j]))
            while currCost>maxCost:
                currCost -= abs(ord(s[i])-ord(t[i]))
                i+=1
            maxi = max(maxi,j-i+1)
            j+=1
        return maxi