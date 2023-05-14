class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch, freq in sorted(count.items(), key=lambda a: -a[1]):
            ans = ans + (ch * freq)

        return ans
