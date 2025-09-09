class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        total //= 2
        dp = set()
        dp.add(0)

        for num in nums:
            curr_dp = set()
            for curr in dp:
                if curr + num == total:
                    return True
                if curr + num < total:
                    curr_dp.add(curr + num)
                curr_dp.add(curr)
            dp = curr_dp
        
        return False

        

        