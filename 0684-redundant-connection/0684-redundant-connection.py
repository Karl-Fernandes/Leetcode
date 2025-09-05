class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            curr = node
            while curr != par[curr]:
                par[curr] = par[par[curr]]
                curr = par[curr]
            
            return curr
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return [n1, n2]
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p2] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
            return None
            
        res = []
        for u, v in edges:
            current_res = union(u, v)
            if current_res:
                res.append(current_res)
        
        return res[-1]
        

        
        

