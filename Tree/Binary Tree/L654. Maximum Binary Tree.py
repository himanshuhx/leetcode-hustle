class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def getIdxOfMax(start, end):
            idx, maxi = start, -float("inf")
            for i in range(start, end+1):
                if nums[i] > maxi:
                    maxi = nums[i]
                    idx = i
            return idx
        
        def dfs(start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(nums[start])
            
            idx = getIdxOfMax(start, end)
            root = TreeNode(nums[idx])
            root.left = dfs(start, idx-1)
            root.right = dfs(idx+1, end)
            return root        
        
        return dfs(0, len(nums)-1)