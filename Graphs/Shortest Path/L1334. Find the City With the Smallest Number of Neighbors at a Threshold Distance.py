class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)

        def build_graph(edges):
            def add_edge(u, v, w):
                graph[u].append((v, w))

            for u, v, w in edges:
                add_edge(u, v, w)
                add_edge(v, u, w)

        def bfs(source):
            heap = []
            cost = [float('inf') for i in range(n)]
            cost[source] = 0
            heapq.heappush(heap, (0, source))

            count = 0
            while heap:
                weight, node = heapq.heappop(heap)

                for adj_node, adj_node_weight in graph[node]:
                    if cost[node] + adj_node_weight < cost[adj_node]:
                        cost[adj_node] = cost[node] + adj_node_weight
                        heapq.heappush(heap, (cost[adj_node], adj_node))

            count = 0
            print(cost)
            for c in cost:
                if c <= distanceThreshold:
                    count += 1
            return count-1

        build_graph(edges)

        mini = 10000000
        res = 0
        for i in range(n):
            c = bfs(i)
            if c <= mini:
                mini = c
                res = i

        return res
