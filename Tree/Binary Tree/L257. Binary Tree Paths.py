class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, path):
            if not root: return
            if not root.left and not root.right:
                paths.append(path[:] + str(root.val))
                return
            dfs(root.left, path + str(root.val) + "->" )
            dfs(root.right, path + str(root.val) + "->" )
        
        paths = []
        dfs(root, "")
        return paths