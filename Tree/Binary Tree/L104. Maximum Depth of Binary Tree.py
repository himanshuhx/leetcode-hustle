# this traversal template

class Solution:
    def maxDepth(self, root) -> int:
        def dfs(root, depth):
            if not root: return 0           
            if not root.left and not root.right: return depth + 1
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))        
        
        return dfs(root, 0)