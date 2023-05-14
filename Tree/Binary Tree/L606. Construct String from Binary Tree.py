class Solution:
    def tree2str(self, t) -> str:
        if t is None:
                return ""
            
        ans = str(t.val) 

        if t.left:
            ans+="(" + self.tree2str(t.left) + ")"

        if not t.left and t.right:
            ans+="()"

        if t.right:
            ans+="(" + self.tree2str(t.right) + ")"

        return ans