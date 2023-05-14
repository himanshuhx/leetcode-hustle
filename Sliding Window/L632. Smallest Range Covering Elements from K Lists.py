import collections
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        sor = []
        K = len(nums)
        count = collections.defaultdict(int)
        for i, num in enumerate(nums):
            for n in num:
                sor.append([n, i])
        sor.sort(key=lambda x: x[0])
        print(sor)
        
        res = []
        i, j = 0, 0
        while j<len(sor):
            count[sor[j][1]] += 1
            while len(count)==K:
                if not res or sor[j][0]-sor[i][0]<res[1]-res[0]:
                    res = [sor[i][0], sor[j][0]]
                count[sor[i][1]] -= 1
                if count[sor[i][1]]==0:
                    count.pop(sor[i][1])
                i += 1
            j+=1
        return res        
    
    
    
    
    
    
    