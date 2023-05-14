class Solution:

    # O(N^2) for each node counting paths
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        def countPathSum(root, currSum):
            if not root: return
            currSum += root.val
            if currSum == target:
                self.count += 1
            countPathSum(root.left, currSum)
            countPathSum(root.right, currSum)
        
        def dfs(root):
            if not root: return           
            countPathSum(root, 0)
            dfs(root.left)
            dfs(root.right)
                
        self.count = 0
        dfs(root)
        return self.count 
    
    # O(N) similar to subarrays of size k
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:        
        def dfs(root, currSum):
            if not root: return           
            currSum += root.val
            
            if currSum-target in self.map:
                self.count += self.map[currSum-target]
            if currSum in self.map:
                self.map[currSum] += 1
            else:
                self.map[currSum] = 1
                
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            
            self.map[currSum] -= 1
                
        self.count = 0
        self.map = {0:1}
        dfs(root, 0)
        return self.count 