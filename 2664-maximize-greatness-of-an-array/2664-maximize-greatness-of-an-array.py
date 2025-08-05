from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        res = 0
        
        pointer1 = 0  # pointer for original sorted array
        pointer2 = 0  # pointer for candidate numbers
        
        while pointer1 < n and pointer2 < n:
            if sorted_nums[pointer2] > sorted_nums[pointer1]:
                res += 1
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2 += 1
        
        return res
