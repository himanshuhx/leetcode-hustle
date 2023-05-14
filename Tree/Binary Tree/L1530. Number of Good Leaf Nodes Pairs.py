class Solution:
    def countPairs(self, root: TreeNode, d: int) -> int:
        def dfs(root):
            if not root: return [0]
            if not root.left and not root.right: return [1]
            
            left_leaf_node_dist = dfs(root.left)
            right_leaf_node_dist = dfs(root.right)
            
            for left_leaf_dist in left_leaf_node_dist:
                for right_leaf_dist in right_leaf_node_dist:
                    
                    if left_leaf_dist and right_leaf_dist and left_leaf_dist + right_leaf_dist <= d:
                        self.count += 1
            
            res = []
            for left_leaf_dist in left_leaf_node_dist:
                if left_leaf_dist and left_leaf_dist+1<d:
                    res.append(left_leaf_dist+1)
                
            for right_leaf_dist in right_leaf_node_dist:
                if right_leaf_dist and right_leaf_dist+1<d:
                    res.append(right_leaf_dist+1)
                
            return res        
        
        self.count = 0
        dfs(root)
        return self.count