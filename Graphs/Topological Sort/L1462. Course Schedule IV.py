class Solution:
    def checkIfPrerequisite(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        @lru_cache
        def bfs(node, target):
            queue = deque()
            queue.append(node)
            visited = set()
            visited.add(node)

            while queue:
                node = queue.popleft()

                if node == target:
                    return True

                for adj_node in graph[node]:
                    if adj_node not in visited:
                        queue.append(adj_node)
                        visited.add(adj_node)

            return False

        graph = [[] for i in range(n)]
        res = []

        for u, v in edges:
            graph[u].append(v)

        for u, v in queries:
            if v in graph[u]:
                res.append(True)
            else:
                res.append(bfs(u, v))

        return res
