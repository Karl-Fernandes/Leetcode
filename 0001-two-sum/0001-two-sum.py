class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, val in enumerate(nums):
            if (target - val) in visited:
                return [visited[target - val], i]
            
            visited[val] = i
        
        