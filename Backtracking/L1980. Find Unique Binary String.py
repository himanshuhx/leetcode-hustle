class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def solve(k, curr):
            if notPresent:
                return
            if k==0:
                temp = ''.join(curr)
                if temp not in present:
                    notPresent.append(temp)
                return
            for value in "01":
                curr.append(value)
                solve(k-1, curr)
                curr.pop()
        
        present = set(nums)
        notPresent = []
        solve(len(nums), [])
        return notPresent[0]