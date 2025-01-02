class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, 0
        res = 0
        n = len(nums)

        while r < n:
            if nums[r] - nums[l] > nums[l]:
                l += 1
                continue

            for i in range(l, r):
                res = max(res, nums[i] ^ nums[r])

            r += 1

        return res  