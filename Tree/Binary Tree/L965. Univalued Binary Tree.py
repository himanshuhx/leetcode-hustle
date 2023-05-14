class Solution:
    def isUnivalTree(self, root) -> bool:
        def dfs(root, value):
            if not root: return True
            if root.val != value: return False
            return dfs(root.left, value) and dfs(root.right, value)
        
        return dfs(root, root.val)