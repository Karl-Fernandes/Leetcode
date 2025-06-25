class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        min_length = float('inf')
        left = 0

        for right in range(0, len(nums)):
            total += nums[right]

            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
          
        
        return min_length if min_length != float('inf') else 0


        