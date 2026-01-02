class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 1
        jumps = 0
        furthest_index = 0

        while r < len(nums):
            for i in range(l, r):
                furthest_index = max(furthest_index, nums[i] + i)
            jumps += 1
            l = r
            r = furthest_index + 1
        
        return jumps
            

