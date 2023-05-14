class Solution:

    # will still call this approach as brute as for each root whose value is equal to subroot
    # we are checking that can it form a possible subtree or not
    def isSubtree(self, root, subRoot) -> bool:
        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return isSame(root1.left, root2.left) and isSame(root1.right,root2.right)
        
        def dfs(root):
            if not root: return False
            if root.val == subRoot.val:
                if isSame(root, subRoot): return True
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)