from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
            
        queue = deque()
        queue.append((root, 1))
        curr_depth = 1
        while queue:
            for i in range(len(queue)):
                
                node, node_depth = queue.popleft()
                if curr_depth == depth - 1:
                    
                    left_root = TreeNode(val)
                    right_root = TreeNode(val)
                    
                    curr_node_left = node.left
                    curr_node_right = node.right
                    
                    node.left = left_root
                    left_root.left = curr_node_left
                    node.right = right_root
                    right_root.right = curr_node_right
                    
                if node.left:
                    queue.append((node.left,curr_depth))
                if node.right:
                    queue.append((node.right,curr_depth))
                    
            curr_depth += 1
            if curr_depth == depth: break
        return root
            