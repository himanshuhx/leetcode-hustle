class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, l, r):
            nonlocal maxi
            if root:
                maxi = max(maxi, l, r)
                dfs(root.left, 0, l+1)
                dfs(root.right, r+1, 0)
                
        maxi = 0
        dfs(root, 0, 0)
        return maxi