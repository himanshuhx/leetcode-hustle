class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxi):
            if not root: return
            if root.val >= maxi:
                self.ans += 1
            dfs(root.left, max(maxi, root.val))
            dfs(root.right, max(maxi, root.val))
        
        self.ans = 0
        dfs(root, -float("inf"))
        return self.ans