class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # build the graph
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))
        
        prob = [0.0] * n
        prob[start_node] = 1.0

        # Max-heap (store negative probabilities to simulate max-heap)
        queue = [(-1.0, start_node)]
        
        while queue:
            current_prob, u = heapq.heappop(queue)
            current_prob = -current_prob  # back to positive

            if u == end_node:
                return current_prob
            
            if current_prob < prob[u]:
                continue
            
            for v, edge_prob in graph[u]:
                new_prob = current_prob * edge_prob
                if new_prob > prob[v]:
                    prob[v] = new_prob
                    heapq.heappush(queue, (-new_prob, v))
        
        return 0.0




        