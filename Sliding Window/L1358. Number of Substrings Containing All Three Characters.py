class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i, j, count = 0, 0, 0
        map = {'a':0,'b':0,'c':0}
        while j<len(s):
            map[s[j]] += 1
            while all(map.values()):
                count += len(s) - j
                map[s[i]] -= 1
                i+=1
            j+=1
        return count