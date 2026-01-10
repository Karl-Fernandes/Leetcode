class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph_nodes = []
        graph = defaultdict(list)
        distances = defaultdict(list)

        for start, end, time in times:
            graph[start].append((end, time))


        for i in range(1, n + 1):
            if i != k:
                heapq.heappush(graph_nodes, (float('inf'), i))
                distances[i] = float('inf')
            else:
                heapq.heappush(graph_nodes, (0, i))
                distances[i] = 0
            


        while graph_nodes:
            _, current_node = heapq.heappop(graph_nodes)
            for neighbour, time in graph[current_node]:
                if distances[current_node] + time < distances[neighbour]:
                    distances[neighbour] = distances[current_node] + time
                    heapq.heappush(graph_nodes, (distances[current_node] + time, neighbour))
        
        largest_distance = max(distances.values())
        if largest_distance == float('inf'):
            return -1
        
        return largest_distance
                


        

            

        