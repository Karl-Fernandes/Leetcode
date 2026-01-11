class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        N = len(points)


        for i in range(N):
            for j in range(i + 1, N):
                if i != j:
                    distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    graph[i].append([distance, j])
                    graph[j].append([distance, i])
        
        res = 0
        visited = set()
        min_heap = [[0, 0]]

        while len(visited) < N:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            
            res += cost
            visited.add(i)

            for neiCost, nei in graph[i]:
                if nei not in visited:
                    heapq.heappush(min_heap, [neiCost, nei])
        
        return res

        
        
        

                    

        