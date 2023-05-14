class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = collections.Counter(s1)
        i, j = 0, 0
        while j<len(s2):
            if j-i+1<len(s1):
                j+=1
            elif j-i+1==len(s1):
                if collections.Counter(s2[i:j+1])==count:
                    return True
                i+=1
                j+=1
        return False
        