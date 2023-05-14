class Solution:
    def findTilt(self, root) -> int:
        def dfs(root):
            nonlocal tilt
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            tilt += abs(left-right)
            return left + right + root.val
        
        tilt = 0
        dfs(root)
        return tilt