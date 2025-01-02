class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        res = current_sum / k

        for i in range (k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            avg = current_sum / k
            res = max(res, avg)
        
        return res

        