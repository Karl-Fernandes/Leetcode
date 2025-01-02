class Solution(object):
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0

        nums.sort()
        min_diff = max(nums)
        for i in range(0, len(nums) - k + 1):
            min_diff = min(min_diff, abs(nums[i] - nums[i + k - 1]))
        
        return min_diff