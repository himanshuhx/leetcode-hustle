class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def check():
            count = 0
            for freq in self.freq:
                if freq % 2: count += 1
            if count == 1 or count == 0: return True
            return False
            
        def dfs(root, path):
            if not root: return
            self.freq[root.val] += 1
            if not root.left and not root.right:
                if check(): self.count += 1
            dfs(root.left, path)
            dfs(root.right, path)
            self.freq[root.val] -= 1
        
        self.count = 0
        self.freq = [0]*10
        dfs(root, [])
        return self.count