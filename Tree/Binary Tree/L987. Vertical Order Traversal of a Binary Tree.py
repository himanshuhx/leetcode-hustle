class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def generateMap(root, hd, level):
            if not root: return
            if hd in self.map:self.map[hd].append([root.val, level])
            else: self.map[hd] = [[root.val,level]]
                
            generateMap(root.left, hd-1, level+1)
            generateMap(root.right, hd+1, level+1)
        
        
        self.map = {}
        generateMap(root, 0, 0)
        ans = []
        for key in sorted(self.map.keys()):
            self.map[key].sort(key = lambda a : a[0])
            self.map[key].sort(key = lambda a : a[1])
            level = []
            for value in self.map[key]:
                    level.append(value[0])
            ans.append(level)
        return ans