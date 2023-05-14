class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, nodeSum):
            if not root: return False
            if not root.left and not root.right and root.val == nodeSum: return True
            
            return dfs(root.left,nodeSum - root.val) or dfs(root.right, nodeSum - root.val)
        
        return dfs(root, targetSum) if root else False