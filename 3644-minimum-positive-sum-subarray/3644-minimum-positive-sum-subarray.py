class Solution:
    def minimumSumSubarray(self, nums, l, r):
        minSum = float('inf')
        for i in range(l, r + 1):
            currSum = 0

            for j in range(i):
                currSum += nums[j]
            if currSum > 0:
                minSum = min(minSum, currSum)

            low, high = 0, i

            while high < len(nums):
                currSum -= nums[low]
                currSum += nums[high]

                low += 1
                high += 1

                if currSum > 0:
                    minSum = min(minSum, currSum)

        if minSum == float('inf'):
            return -1
        return minSum