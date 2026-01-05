class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_indices = {}
        res = []

        for i, v in enumerate(s):
            end_indices[v] = i
        
        end = end_indices[s[0]]
        start = 0

        for i, v in enumerate(s):
            if end_indices[v] > end:
                end = end_indices[v]

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res
            

            

        