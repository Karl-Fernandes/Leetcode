class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i in range(3):
                    res[i] = max(res[i], t[i])
            
            if (res == target):
                return True
        
        return all((x == y) for x, y in zip(res, target))
                                          
      