class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q: return True
        if not p: return False
        if not q: return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False