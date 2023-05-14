from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def generateParent(root):
            if not root: return
            self.parentOf[root.left] = root
            self.parentOf[root.right] = root
            if root.val == startValue: self.start = root
            generateParent(root.left)
            generateParent(root.right)
    
            
        self.parentOf = {}
        self.start = None
        generateParent(root)
        
        queue, visited = deque(), set()
        queue.append((self.start, ""))

        while queue:
            for i in range(len(queue)):
                node, path = queue.popleft()
                if node and node.val == destValue:
                    return path
                if node.left and node.left not in visited:
                    queue.append((node.left, path+"L"))
                if node.right and node.right not in visited:
                    queue.append((node.right, path+"R"))
                if node in self.parentOf and self.parentOf[node] not in visited:
                    queue.append((self.parentOf[node], path+"U"))
                visited.add(node)

# optimized approach is to find lca and do a bfs