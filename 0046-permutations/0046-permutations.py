class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num in curr:
                    continue
                
                curr.append(num)
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return res


        