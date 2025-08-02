class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        

        def dfs(visited):
            if len(visited) == len(nums):
                res.append(visited.copy())
                return

            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                    
                visited.append(nums[i])
                dfs(visited)
                visited.pop()
                

        dfs([])
        return res            
        
