class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def solve():
            if len(perm)==len(nums):
                ans.append(perm[:])
                return
            for x in counter:
                if counter[x]>0:
                    perm.append(x)
                    counter[x]-=1
                    solve()
                    perm.pop()
                    counter[x]+=1

        counter = {}
        for n in nums:
            if n in counter:
                counter[n]+=1
            else:
                counter[n]=1
        ans = []
        perm = []
        solve()
        return ans