class Solution:


    # despite of checking and swaping at each stage we can just check whether the value stands
    # out to be true if flipped or if not flipped.
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if root1==None and root2==None: return True
            
            if not root1 or not root2 or root1.val != root2.val: return False
            
            if dfs(root1.left,root2.right) and dfs(root1.right, root2.left):
                return True
            
            
            if dfs(root1.left, root2.left) and dfs(root1.right, root2.right):
                return True

        return dfs(root1, root2)