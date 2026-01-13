class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DIRECTIONS = [[0, 1], [1, 0]]
        memo = {}

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0

            if (r, c) == (m - 1, n - 1):
                return 1
            
            if (r, c) in memo:
                return memo[(r, c)]
        
            
            total_paths = 0
            for DR, DC in DIRECTIONS:
                total_paths += dfs(r + DR, c + DC)
            memo[(r, c)] = total_paths 
            return total_paths

        return dfs(0, 0)
            