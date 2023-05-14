class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root: return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            flag = False
            if root.val == 1 or root.left or root.right:
                flag = True
            
            return root if flag else None
        
        
        return dfs(root)