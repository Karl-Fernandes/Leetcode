class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), cost in zip(equations, values):
            graph[u].append((v, cost))
            graph[v].append((u, cost ** -1))

        

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            queue = deque([(start, 1.0)])  # (node, cumulative product)
            visited = set()

            while queue:
                node, product = queue.popleft()

                if node == end:
                    return product
                
                visited.add(node)
                for v, cost in graph[node]:
                    if v not in visited:
                        queue.append((v, product * cost))
            
            return -1.0
        
        return [bfs(u, v) for u, v in queries]
            




