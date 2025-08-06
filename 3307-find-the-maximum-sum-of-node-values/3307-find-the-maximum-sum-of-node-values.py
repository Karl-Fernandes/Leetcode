class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        xorCnt = res = 0
        minDiff = 1 << 20

        for num in nums:
            xorNum = num ^ k
            if xorNum > num:
                res += xorNum
                xorCnt ^= 1
            else:
                res += num
            minDiff = min(minDiff, abs(xorNum - num))

        return res - xorCnt * minDiff