class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:       
        graph = {}
        indegree = [0]*n
        for req in prerequisites:
            graph[req[1]] = graph.get(req[1], []) + [req[0]]
            indegree[req[0]] += 1
            
        q = collections.deque()
        count = 0

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            node = q.popleft()
            count += 1
            
            for adj_node in graph[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node]==0:
                    q.append(adj_node)
                              
        return count == n
            