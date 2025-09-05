class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = 0
        res = 0
        
        for num in nums:
            total += num
            if total > 0:
                res += 1
        
        return res


        