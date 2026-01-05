class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                res = (max(x, y) for x, y in zip(t, res))
        
        return all((x == y) for x, y in zip(res, target))
                                          
      