class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        time = 0
        q = deque()

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        
        def rotten(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return False
            
            grid[r][c] = 2
            q.append([r, c])
            return True

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    if rotten(r + dr, c + dc):
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1

        