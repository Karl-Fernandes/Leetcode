class Solution(object):
    def findLHS(self, nums):
        nums.sort()  
        l = 0  
        max_length = 0  
        n = len(nums)

        for r in range(n):
            while nums[r] - nums[l] > 1:
                l += 1
            
            # If the difference is exactly 1, calculate the length
            if nums[r] - nums[l] == 1:
                max_length = max(max_length, r - l + 1)

        return max_length
