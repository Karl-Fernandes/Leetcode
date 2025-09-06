class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [u for u in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            current = node

            while current != parent[current]:
                parent[current] = parent[parent[current]]
                current = parent[current]

            return current
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return [n1, n2]
            
            if p1 > p2:
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1
            
            return None
        
        res = []
        for u, v in edges:
            curr_res = union(u, v)
            if curr_res:
                res.append(curr_res)


        return res[-1]
            