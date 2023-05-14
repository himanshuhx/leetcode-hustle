class Solution:

    # approach - find the path to target nodes
    # then find the firt non common
    # if all are common we know one of the node is direct descendent of other node
    # so that node is ans (last common node)
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root, node, path):
            if not root: return False
            path.append(root)
            if root.val == node.val: return True
            
            if dfs(root.left, node, path) or dfs(root.right, node, path): return path            
            path.pop()
            
            return False
        
        path1, path2 = [], []
        dfs(root, p, path1)
        dfs(root, q, path2)
        
        prev = None
        for i in range(min(len(path1), len(path2))):
            if path1[i]!=path2[i]:
                return prev
            prev = path1[i]
        return prev



    # Optimized approach
    # if any of the p or q found return root
    # if nothing is found and we reached leaf return None
    # if both are recieved than the current root is lca return it
    # if any one is not null either left or right we can conclude that this root is a lca
    # which is direct descendent of other node.  ex- 2->3->5 p=2 q=5  2 is lca of 2 and 5
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root):
            if not root: return None
            if root.val == p.val or root.val == q.val: return root
                        
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right: return root
            if left: return left
            if right: return right
        
        return dfs(root)