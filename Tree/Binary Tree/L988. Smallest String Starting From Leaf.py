class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root, curr):
            nonlocal res
            if not root: return
            if not root.left and not root.right:
                curr += [chr(root.val + 97)]
                if not res:
                    res = curr[::-1]
                else:
                    res = min(res, curr[::-1])
                    
            dfs(root.left, curr + [chr(root.val + 97)])
            dfs(root.right, curr + [chr(root.val + 97)])
            
        res = []
        dfs(root, [])
        return "".join(res)
        