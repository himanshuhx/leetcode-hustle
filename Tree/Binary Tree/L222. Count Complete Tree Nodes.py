class Solution:
# O(N), O(logn)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            dfs(root.right)
            self.count += 1
        
        self.count = 0
        dfs(root)
        return self.count


# Time complexity - O(logn*logn), space complexity - O(logn)
# maximum height of a complete binary tree can be logn.
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getLeftHeight(root):
            h = 0
            while root:
                root = root.left
                h += 1
            return h
        
        def getRightHeight(root):
            h = 0
            while root:
                root = root.right
                h += 1
            return h
        
        def dfs(root):
            if not root: return 0
            leftHeight = getLeftHeight(root)
            rightHeight = getRightHeight(root)
            
            if leftHeight == rightHeight:
                return 2**leftHeight - 1
            return 1 + dfs(root.left) + dfs(root.right)
            
        return dfs(root)