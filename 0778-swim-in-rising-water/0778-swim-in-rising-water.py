class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        while pq:
            curr_max_height, r, c = heapq.heappop(pq)

            if r == n - 1 and  c == n - 1:
                return curr_max_height
            
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    max_cost = max(grid[nr][nc], curr_max_height)
                    heapq.heappush(pq, (max_cost, nr, nc))
                    visited.add((nr, nc))
        


        