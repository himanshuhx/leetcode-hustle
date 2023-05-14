class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check(root, curr):
            if not curr: return True
            if not root: return False
            if root.val == curr.val:
                return check(root.left, curr.next) or check(root.right, curr.next)
            return False
        
        def dfs(root):
            if not root: return False
            if root.val == head.val:
                curr = head
                if check(root, curr): return True
            return dfs(root.left) or dfs(root.right)        
        
        return dfs(root)