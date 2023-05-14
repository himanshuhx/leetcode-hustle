class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        def build_graph(equations, values):
            def add_edge(u, v, value):
                if u in graph:
                    graph[u].append((v, value))
                else:
                    graph[u] = [(v, value)]

            for edges, value in zip(equations, values):
                u, v = edges
                add_edge(u, v, value)
                add_edge(v, u, 1/value)

        def bfs(query):
            u, v = query
            if u not in graph or v not in graph:
                return -1.00000

            queue = deque()
            visited = set()
            queue.append((u, 1.0))

            while queue:
                node, curr_product = queue.popleft()
                if node == v:
                    return curr_product
                visited.add(node)
                for adj_node, adj_node_value in graph[node]:
                    if adj_node not in visited:
                        queue.append((adj_node, curr_product*adj_node_value))
            return -1.00000

        build_graph(equations, values)

        res = []
        for query in queries:
            res.append(bfs(query))

        return res
