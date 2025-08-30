class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        res = []
        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)
            for v in graph[crs]:
                if not dfs(v):
                    return False
            
            res.append(crs)
            visited.add(crs)
            visiting.remove(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
        