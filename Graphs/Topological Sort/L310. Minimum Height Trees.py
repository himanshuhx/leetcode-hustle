class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        indegree = [0]*n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[v]+=1
            indegree[u]+=1
            
        queue = deque()
        res = []
        
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
                indegree[i] -= 1
                
        while queue:
            res.clear()
            for i in range(len(queue)):
                node = queue.popleft()           
                res.append(node)
                
                for adj_node in graph[node]:
                
                    indegree[adj_node] -= 1
                    if indegree[adj_node] == 1:
                        queue.append(adj_node)
                    
        return res if res else [0]