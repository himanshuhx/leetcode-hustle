class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, currSum):
            if not root: return
            if not root.left and not root.right:
                self.ans += currSum*10 + root.val
                return 
            currSum = currSum * 10 + root.val
            dfs(root.left, currSum)
            dfs(root.right, currSum)
        
        self.ans = 0
        dfs(root, 0)
        return self.ans