class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, curr_sum, path):
            if not root: return
            if not root.left and not root.right:
                if curr_sum + root.val == targetSum:
                    path.append(root.val)
                    self.paths.append(path[:])
                    path.pop()
                    return
            path.append(root.val)
            dfs(root.left, curr_sum + root.val, path)
            dfs(root.right, curr_sum + root.val, path)
            path.pop()
            
        self.paths = []
        dfs(root, 0, [])
        return self.paths