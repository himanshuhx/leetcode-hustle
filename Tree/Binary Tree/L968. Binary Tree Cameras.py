class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return "this_node_is_covered_by_its_child"
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            if l == "please_cover_me" or r == "please_cover_me":
                self.camera += 1
                return "child_now_have_camera"
            
            if l == "child_now_have_camera" or r == "child_now_have_camera":
                return "this_node_is_covered_by_its_child" 
            
            return "please_cover_me"
        
        self.camera = 0
        
        return self.camera+1 if dfs(root) == "please_cover_me" else self.camera