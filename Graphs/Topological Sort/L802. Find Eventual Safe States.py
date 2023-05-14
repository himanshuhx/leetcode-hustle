class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        inv_graph = [[] for i in range(n)]
        indegree = [0]*n

        for v in range(len(graph)):
            for u in graph[u]:
                inv_graph[u].append(v)
                indegree[v] += 1

        queue = deque()
        res = []

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.append(node)

            for adj_node in inv_graph[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        res.sort()
        return res
