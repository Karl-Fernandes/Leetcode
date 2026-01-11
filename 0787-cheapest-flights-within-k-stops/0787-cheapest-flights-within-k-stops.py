class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        prices = [float("inf")] * n
        prices[src] = 0

        for u, v, cst in flights:
            graph[u].append((v, cst))

        
        q = deque([(0, src, 0)])
        while q:
            cst, node, stops = q.popleft()

            if stops > k:
                continue
            
            for nei, neiCost in graph[node]:
                nextCost = neiCost + cst
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))
        
        return prices[dst] if prices[dst] != float('inf') else -1

