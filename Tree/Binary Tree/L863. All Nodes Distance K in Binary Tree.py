from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:          
        def generate_map(root):
            if not root: return           
            if root.left: child_to_parent[root.left] = root
            if root.right: child_to_parent[root.right] = root                
            generate_map(root.left)
            generate_map(root.right)
        
        ans = []
        child_to_parent = defaultdict()
        generate_map(root)
        
        queue = deque()
        queue.append(target)
        visited = set()
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                
                if k==0: ans.append(node.val)
                
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                if node in child_to_parent and child_to_parent[node] not in visited:
                    queue.append(child_to_parent[node])
                    
            if k == 0: break
            k -= 1
            
        return ans