class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if i ==  len(graph) - 1:
                res.append(curr.copy())
                return
            
            for nei in graph[i]:
                curr.append(nei)
                dfs(nei, curr)
                curr.pop()
        
        dfs(0, [0])
        return res
        