import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def validWindow(mapS, mapT):
            count=0
            for key in mapT:
                if key in mapS and mapS[key]>=mapT[key]:
                    count+=1
            return count==len(mapT)
        
        if len(s)<len(t):
            return ""
        mapT = collections.Counter(t)
        i, j = 0, 0
        mapS = collections.defaultdict(int)
        ans, mini = "", float("inf")
        while j<len(s):
            mapS[s[j]] += 1
            while validWindow(mapS,mapT):
                if mini>j-i+1:
                    ans = s[i:j+1]
                    mini = j-i+1
                mapS[s[i]]-=1
                i+=1                
            j+=1
        return ans