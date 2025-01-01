class Solution(object):
    def XSum(self, nums, x):
        # Count occurrences
        XSum = {}
        for num in nums:
            if num not in XSum:
                XSum[num] = 1
            else:
                XSum[num] += 1

        sorted_items = sorted(XSum.items(), key=lambda item: (item[1], item[0]), reverse=True)

        top_two_sum = sum(freq * num for num, freq in sorted_items[:x])
        return top_two_sum

    def findXSum(self, nums, k, x):
        answer = []
        for l in range(len(nums) - k + 1):
            subarray = nums[l:l + k]
            answer.append(self.XSum(subarray, x))

        return answer


