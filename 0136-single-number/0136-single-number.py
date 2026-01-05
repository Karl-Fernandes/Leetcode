class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = {}

        for num in nums:
            if num in visited:
                visited[num] += 1
            else:
                visited[num] = 1
        
        print(visited)
        return min(visited, key=visited.get)