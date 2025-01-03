class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        if not nums:
            return 0
        
        l = 0 
        r = 0 
        longest = 0 

        while r < len(nums):
            if nums[r] % 2 == 0 and nums[r] <= threshold:
                l = r 

                
                while r + 1 < len(nums) and nums[r] % 2 != nums[r + 1] % 2 and nums[r + 1] <= threshold:
                    r += 1 
                longest = max(longest, r - l + 1) 
            r += 1 
        
        return longest