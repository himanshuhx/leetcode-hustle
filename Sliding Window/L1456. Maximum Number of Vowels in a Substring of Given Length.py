class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, j = 0, 0
        ans, count = -float("inf"), 0
        vowels = set(['a','e','i','o','u'])
        while j<len(s):
            if s[j] in vowels:
                count += 1
            if j-i+1==k:
                ans = max(ans,count)
                if s[i] in vowels:
                    count-=1
                i+=1            
            j+=1
        return ans