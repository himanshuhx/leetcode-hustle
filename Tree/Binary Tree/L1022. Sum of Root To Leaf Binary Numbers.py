class Solution:
    def sumRootToLeaf(self, root) -> int:        
        def dfs(root, s):
            if not root: return 0            
            s = s << 1 
            s += root.val
            if not root.left and not root.right: return s
            return dfs(root.left, s) + dfs(root.right, s)
            
        return dfs(root, 0)
        
            