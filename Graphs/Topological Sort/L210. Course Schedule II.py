class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        indegree = [0]*n
        res = []

        for v, u in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.append(node)

            for adj_node in graph[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        return res if len(res) == n else []

    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node):
            indegree[node] -= 1
            res.append(node)
            for adj_node in graph[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    dfs(adj_node)

        graph = [[] for i in range(n)]
        indegree = [0]*n
        res = []

        for v, u in edges:
            graph[u].append(v)
            indegree[v] += 1

        for i in range(n):
            if indegree[i] == 0:
                dfs(i)

        return res if len(res) == n else []
