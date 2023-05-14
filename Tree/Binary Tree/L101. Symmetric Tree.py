class Solution:
    def isSymmetric(self, root) -> bool:
        def dfs(left, right):
            if not left and not right: return True
            if not left or not right: return False
            if left.val != right.val: return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        
        if not root: return True
        return dfs(root, root)