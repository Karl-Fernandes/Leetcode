from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        DIRECTIONS = [
            (0, 1), (1, 0), (0, -1), (-1, 0), 
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        
       
        q = deque([(0, 0, 1)]) 
        grid[0][0] = 1 

        while q:
            r, c, dist = q.popleft()

            if (r, c) == (n - 1, n - 1):
                return dist

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc

                # Bounds check AND Valid path check
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    q.append((nr, nc, dist + 1))
                    grid[nr][nc] = 1

        return -1