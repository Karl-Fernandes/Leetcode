class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return 
                
            if i == len(candidates) or total > target:
                return
            
            

            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
        
    

        dfs(0, 0)
        return res