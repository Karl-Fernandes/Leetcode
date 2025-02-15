from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize m as a list containing only the first element
        res = max(nums)
        maxRes, minRes = 1, 1

        for num in nums:
            tmp = maxRes * num
            maxRes = max(num * maxRes, num * minRes, num)
            minRes = min(tmp, num * minRes, num)

            res = max(maxRes, minRes, res)

        return res 
