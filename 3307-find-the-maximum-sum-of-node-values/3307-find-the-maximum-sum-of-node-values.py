class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        dp = [0, float("-inf")]

        for i in range(len(nums) - 1, -1, -1):
            next_dp = [0, 0]
            next_dp[0] = max(nums[i] + dp[0], (nums[i] ^ k) + dp[1])
            next_dp[1] = max(nums[i] + dp[1], (nums[i] ^ k) + dp[0])
            dp = next_dp

        return dp[0]