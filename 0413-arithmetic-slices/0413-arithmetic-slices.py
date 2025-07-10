class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        r = 1

        if n < 3:
            return 0

        while r < n:
            distance = nums[r] - nums[r - 1]
            start_pos = r - 1 
            
            while r < n and nums[r] - nums[r - 1] == distance:
                r += 1
            
            length = r - start_pos
            
            if length >= 3:
                res += (length - 2) * (length - 1) // 2

        return res