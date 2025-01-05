class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        res = 0
        max_deque = []  
        min_deque = []  

        for r in range(len(nums)):
            while max_deque and nums[max_deque[-1]] <= nums[r]:
                max_deque.pop()
            max_deque.append(r)

            while min_deque and nums[min_deque[-1]] >= nums[r]:
                min_deque.pop()
            min_deque.append(r)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                
                if max_deque[0] < l:
                    max_deque.pop(0)
                if min_deque[0] < l:
                    min_deque.pop(0)

            res = max(res, r - l + 1)

        return res
