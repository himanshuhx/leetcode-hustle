class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0
            currSum = dfs(root.left) + dfs(root.right) + root.val
            self.ans = max(self.ans, currSum * (self.total - currSum))
            return currSum
        
        self.total, self.ans = 0, 0
        self.total = dfs(root)
        dfs(root)
        return self.ans % (10**9 + 7)