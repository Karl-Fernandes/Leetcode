class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            curMax, curMin = max(curMax * num, curMin * num, num), min(curMax * num, curMin * num, num)
            res = max(curMax, res)
        
        return res
        